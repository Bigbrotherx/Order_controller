from flask_restful import Resource, fields, marshal_with

from .models import Order
from . import logger


resourse_fields = {
    "id": fields.Integer,
    "order_name": fields.Integer,
    "price_usd": fields.Integer,
    "price_rub": fields.Float,
    "expires_in": fields.DateTime(dt_format="iso8601"),
}


class OrderInfo(Resource):
    @marshal_with(resourse_fields)
    def get(self):
        query_set = Order.query.all()
        logger.info(query_set)
        return query_set
