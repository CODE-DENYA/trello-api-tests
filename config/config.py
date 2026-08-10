import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()


class Config:
    API_KEY = os.getenv("TRELLO_API_KEY")
    TOKEN = os.getenv("TRELLO_TOKEN")
    BASE_URL = os.getenv("TRELLO_BASE_URL", "https://api.trello.com/1")

    # Формируем параметры авторизации для каждого REST API запроса
    AUTH_PARAMS = {
        "key": API_KEY,
        "token": TOKEN
    }