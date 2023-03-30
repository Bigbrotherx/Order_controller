from flask_restful import Resource, fields, marshal_with

from .models import Order


class MyDateFormat(fields.Raw):
    """Кастомное поле для отображения даты"""

    def format(self, value):
        return value.strftime("%d.%m.%Y")


class ShortFloat(fields.Raw):
    """
    Кастомное поле для отображения float с округлением до сотых
    """

    def format(self, value):
        return float(f"{value:.2f}")


# Поля сериализатора
resourse_fields = {
    "id": fields.Integer,
    "order_name": fields.Integer,
    "price_usd": fields.Integer,
    "price_rub": ShortFloat,
    "expires_in": MyDateFormat,
}


class OrderInfo(Resource):
    """
    View класс для endpoint: /order-info
    """

    @marshal_with(resourse_fields)
    def get(self):
        """
        Реализация метода GET.
        Декоратор для сериализации данных из ORM.
        """
        query_set = Order.query.all()
        return query_set
