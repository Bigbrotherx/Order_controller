from sqlalchemy import Column, Integer, Date, Float

from . import db


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
                name="order", if_exists="replace", con=db.engine, index=False
            )
        except Exception as e:
            print(e)
