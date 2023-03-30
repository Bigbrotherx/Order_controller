from .models import Order
from .utils import get_data_from_google, get_currency_rate
from .extensions import scheduler


@scheduler.task("interval", id="db_update", seconds=60)
def data_update_rutine():
    data = get_data_from_google()
    name, currency = get_currency_rate()
    if name == "Доллар США":
        with scheduler.app.app_context():
            Order.update_data(data, currency)
