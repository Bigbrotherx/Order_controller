from flask_restful import Resource, fields, marshal_with

from .models import Order
from . import logger


class MyDateFormat(fields.Raw):
    def format(self, value):
        return value.strftime("%d.%m.%Y")


class ShortFloat(fields.Raw):
    def format(self, value):
        return float(f"{value:.2f}")


resourse_fields = {
    "id": fields.Integer,
    "order_name": fields.Integer,
    "price_usd": fields.Integer,
    "price_rub": ShortFloat,
    "expires_in": MyDateFormat,
}


class OrderInfo(Resource):
    @marshal_with(resourse_fields)
    def get(self):
        query_set = Order.query.all()
        logger.info(query_set)
        return query_set
