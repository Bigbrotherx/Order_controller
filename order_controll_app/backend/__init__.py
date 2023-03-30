import logging

from flask import Flask

from .config import DataBaseConfig, AppConfig
from .extensions import db, scheduler, api

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_app():
    app = Flask(
        __name__,
        template_folder=AppConfig.TEMPLATE_DIR,
        static_folder=AppConfig.STATIC_DIR,
    )
    app.config["SECRET_KEY"] = AppConfig.APP_SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = DataBaseConfig.DATABASE_URI
    app.config["SCHEDULER_API_ENABLED"] = AppConfig.SCHEDULER

    db.init_app(app)
    scheduler.init_app(app)

    with app.app_context():
        db.create_all()

        from frontend.views import views

        app.register_blueprint(views, url_prefix="/")

        from . import tasks

        scheduler.start()

        from .views import OrderInfo

        api.add_resource(OrderInfo, "/order-info")
        api.init_app(app)

    return app
