"""Каталог товаров/услуг (учебные данные, цены условные)."""
CATALOG = [
    {"id": "sock", "name": "Умная розетка Wi-Fi", "category": "умный дом", "price": 4500,
     "keywords": ["розетка", "электричество", "включить", "расписание", "энергия"]},
    {"id": "bulb", "name": "Умная лампа RGB", "category": "умный дом", "price": 3500,
     "keywords": ["лампа", "свет", "освещение", "яркость"]},
    {"id": "cam", "name": "Wi-Fi камера наблюдения", "category": "умный дом", "price": 14000,
     "keywords": ["камера", "безопасность", "видео", "наблюдение", "охрана"]},
    {"id": "lock", "name": "Умный замок", "category": "умный дом", "price": 38000,
     "keywords": ["замок", "дверь", "ключ", "доступ"]},
    {"id": "hub", "name": "Умный хаб (центр управления)", "category": "умный дом", "price": 18000,
     "keywords": ["хаб", "управление", "сценарий", "голосовой", "ассистент"]},
    {"id": "eknot_vote", "name": "e-KNOT: онлайн-голосование", "category": "услуга", "price": None,
     "keywords": ["голосование", "собрание", "кворум", "жк", "протокол", "жильцы", "лифт"]},
]

def find_products(text: str, limit: int = 3):
    """Простой подбор: считаем совпадения ключевых слов с текстом клиента."""
    t = text.lower()
    scored = []
    for p in CATALOG:
        score = sum(1 for k in p["keywords"] if k in t)
        if score:
            scored.append((score, p))
    scored.sort(key=lambda x: -x[0])
    return [p for _, p in scored[:limit]]
