import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


class AppConfig:
    """Общая конфигурация Flask приложения"""

    BASE_DIR = Path(__file__).resolve().parent.parent
    TEMPLATE_DIR = BASE_DIR / "frontend" / "templates"
    STATIC_DIR = BASE_DIR / "frontend" / "static"
    APP_SECRET_KEY = os.getenv("SECRET_KEY")
    SCHEDULER = True


class DataBaseConfig:
    """Конфигурация Базы данных"""

    DATA_BASE_NAME = "db_date"
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
    DATABASE_URI = (
        f"postgresql+psycopg2://{DATABASE_USER}:"
        f"{DATABASE_PASSWORD}@0.0.0.0:5432/{DATA_BASE_NAME}"
    )


class GoogleConfig:
    """Конфигурация для API Google"""

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    SERVICE_ACCOUNT_FILE = (
        Path(__file__).resolve().parent
        / "service_files"
        / "order-controller-ae26d5f5c0b4.json"
    )
    FILE_ID = os.getenv("FILE_ID")

    COLUMN_NAMES = [
        "№",
        "заказ №",
        "стоимость,$",
        "срок поставки",
    ]


class TelegramConfig:
    """Конфигурация для API Telegram"""

    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
