from .models import Order
from .utils import get_data_from_google, get_currency_rate
from .extensions import scheduler
from .bot import check_expires_dates


@scheduler.task("interval", id="db_update", seconds=60)
def data_update_rutine():
    """
    Актуализация данных из Google Sheets.
    Запускается раз в минуту.
    """
    data = get_data_from_google()
    name, currency = get_currency_rate()
    if name == "Доллар США":
        with scheduler.app.app_context():
            Order.update_data(data, currency)


@scheduler.task("interval", id="telegram_bot", seconds=60 * 60 * 24)
def telegram_bot_rutine():
    """Отправка просроченных заказов в БОТ раз в сутки"""
    data = get_data_from_google()
    check_expires_dates(data)
