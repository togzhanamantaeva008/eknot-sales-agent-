"""Telegram-бот AI-агент продаж (Gemini). Запуск: python -m bot.telegram_bot"""
import os, logging
from dotenv import load_dotenv
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from bot.catalog import find_products
from prompts import SALES_SYSTEM

load_dotenv()
logging.basicConfig(level=logging.INFO)
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
MODEL = genai.GenerativeModel("gemini-2.0-flash", system_instruction=SALES_SYSTEM)
sessions = {}  # chat_id -> chat session

def fmt(products):
    lines = []
    for p in products:
        price = f"{p['price']} ₸" if p["price"] else "по запросу"
        lines.append(f"• {p['name']} — {price}")
    return "\n".join(lines)

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    sessions[update.effective_chat.id] = MODEL.start_chat()
    await update.message.reply_text(
        "Здравствуйте! Я помощник по продажам. Помогу подобрать решения для умного дома "
        "и онлайн-голосование e-KNOT. Расскажите, что вам нужно?")

async def reset(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    sessions.pop(update.effective_chat.id, None)
    await update.message.reply_text("Диалог сброшен. Напишите /start.")

async def on_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    cid = update.effective_chat.id
    text = update.message.text
    chat = sessions.setdefault(cid, MODEL.start_chat())
    products = find_products(text)
    hint = f"\n[Подходящие позиции из каталога:\n{fmt(products)}]" if products else ""
    try:
        reply = chat.send_message(text + hint).text
    except Exception as e:
        logging.exception("Gemini error")
        reply = "Извините, сервис временно недоступен. Попробуйте позже."
    await update.message.reply_text(reply)

def main():
    app = Application.builder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
    app.run_polling()

if __name__ == "__main__":
    main()
