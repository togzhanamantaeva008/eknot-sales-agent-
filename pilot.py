"""Пилот: руководитель пишет как клиент/менеджер, бот отвечает. Диалог сохраняется в pilot_log.txt"""
import os
from dotenv import load_dotenv
import google.generativeai as genai
from prompts import SALES_SYSTEM

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash", system_instruction=SALES_SYSTEM)
chat = model.start_chat()
print("Пилот басталды. 'exit' — шығу.")
with open("pilot_log.txt", "a", encoding="utf-8") as log:
    while True:
        msg = input("Клиент: ")
        if msg.lower() == "exit":
            break
        reply = chat.send_message(msg).text
        print("Бот:", reply)
        log.write(f"Клиент: {msg}\nБот: {reply}\n\n")
