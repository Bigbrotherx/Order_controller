import datetime as dt

import telegram

from . import logger
from .config import TelegramConfig
from .utils import pd


bot = telegram.Bot(token=TelegramConfig.TELEGRAM_TOKEN)
# Название столбца для даты
EXPIRY_DATE_NAME = "expires_in"
# Название столбца для отправки в бот в случае просрочки
ORDER_NAME = "order_name"


def send_message(bot, message):
    """Функция отправки сообщения в бот."""
    try:
        bot.send_message(chat_id=TelegramConfig.TELEGRAM_CHAT_ID, text=message)
    except telegram.error.TelegramError as error:
        logger.error(f"Сбой отправки: {error}")
    else:
        logger.debug(f"Отправленно сообщение: {message}")


def find_expired_in_timedelta(data_dict, current_date):
    """Поиск заказов с истекшим сроком"""
    clients_list = []
    for row, expiry_date_timestamp in data_dict.get(EXPIRY_DATE_NAME).items():
        expiry_date = pd.to_datetime(expiry_date_timestamp).date()
        if current_date > expiry_date:
            clients_list.append(row)

    return clients_list


def prepare_message_with_clients(data_dict, clients_list):
    """Подготовка сообщения с клиентами из списка"""
    message = ""
    if len(clients_list):
        for number in clients_list:
            client_name = data_dict.get(ORDER_NAME).get(number)
            expiry_date = data_dict.get(EXPIRY_DATE_NAME).get(number)
            message += (
                f"Order number {client_name}." f" expiry date: {expiry_date}\n"
            )

    return message


def check_expires_dates(data):
    """Точка входа для ботавызывается из tasks.py"""
    current_date = dt.date.today()
    data_dict = data.to_dict()
    try:
        orders_list = find_expired_in_timedelta(data_dict, current_date)
        new_message = prepare_message_with_clients(data_dict, orders_list)
        if new_message == "":
            new_message = f"Today {current_date} there are no expiring orders"
        send_message(bot, new_message)
    except Exception as error:
        new_message = f"Bot task finished with error: {error}"
        send_message(bot, new_message)
