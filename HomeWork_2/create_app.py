from flask import Flask
from data import db


def create_app():

    # Конфигурация приложения
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = {'ensure_ancii': False, 'indent': 4}
    #app.config['SQLALCHEMY_ECHO'] = True

    # Конфигурация базы данных
    db.init_app(app)
    app.app_context().push()

    # Инициализация таблиц
    db.create_all()

    return app