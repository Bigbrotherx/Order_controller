from sqlalchemy import Column, Integer, Date, Float

from . import db, logger


class Order(db.Model):
    id = Column(Integer, primary_key=True)
    order_name = Column(Integer, unique=True)
    price_usd = Column(Integer)
    price_rub = Column(Float, nullable=True)
    expires_in = Column(Date)

    def update_data(data_frame, currency_rate):
        data_frame["price_rub"] = [
            int(each_value) * currency_rate
            for each_value in data_frame.price_usd.values
        ]
        try:
            data_frame.to_sql(
                name="order",
                if_exists="replace",
                con=db.engine,
                index=False,
                dtype={
                    "id": Integer(),
                    "order_name": Integer(),
                    "price_usd": Integer(),
                    "price_rub": Float(),
                    "expires_in": Date(),
                },
            )
        except Exception as error:
            logger.error(f"Data base update finished with errors: {error}")
        else:
            logger.info("Data base was successfuly updated")
