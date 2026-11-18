# AI-агент продаж e-KNOT (онлайн-голосование)

Воронка: анализ чата → лид → портрет клиента → холодный контакт → продажа.

## Қосу
```
pip install -r requirements.txt
cp .env.example .env   # GEMINI_API_KEY қойыңыз (aistudio.google.com)
python funnel.py       # воронка, нәтиже results.json
python pilot.py        # пилот: чат-бот менеджер
```

## Құрылым
- `prompts.py` — барлық промпттар
- `funnel.py` — чат талдау, лид, портрет, холодный контакт
- `pilot.py` — сатушы-бот диалогы (пилот)
- `data/chats.json` — тест чаттар (3 мысал: 2 лид, 1 лид емес)

## Келесі қадам
Google Cloud серверіне орналастыру, содан кейін WhatsApp (Cloud API) қосу.

## Telegram-бот
1. В Telegram найдите @BotFather → /newbot → получите токен.
2. В `.env` добавьте `TELEGRAM_BOT_TOKEN=...`
3. Запуск: `python -m bot.telegram_bot`

## Документы
- `docs/TZ.md` — техническое задание
- `docs/scenarios.md` — сценарии общения
- `docs/test_log.md` — журнал проверки

## Тесты
`python tests/test_logic.py`
