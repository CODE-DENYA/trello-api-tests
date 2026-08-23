import os
from typing import ClassVar

from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()


class Config:
    API_KEY = os.getenv("TRELLO_API_KEY")
    TOKEN = os.getenv("TRELLO_TOKEN")
    BASE_URL = os.getenv("TRELLO_BASE_URL", "https://api.trello.com/1")

    # Проверка обязательных переменных
    if not API_KEY or not TOKEN:
        raise ValueError("Ошибка: TRELLO_API_KEY и TRELLO_TOKEN должны быть заданы в .env или Secrets")

    # Формируем параметры авторизации для каждого REST API запроса
    AUTH_PARAMS: ClassVar[dict[str, str]] = {
        "key": API_KEY,
        "token": TOKEN,
    }