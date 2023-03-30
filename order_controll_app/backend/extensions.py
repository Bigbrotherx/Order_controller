"""Initialize any app extensions."""
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from flask_restful import Api

# База данных
db = SQLAlchemy()
# Планировщик задач
scheduler = APScheduler()
# API для связи с frontend приложением
api = Api()
