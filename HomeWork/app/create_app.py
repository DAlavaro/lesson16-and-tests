import json
from flask import Flask

from HomeWork.app import db
from HomeWork.app.models import Offer, Order, User


def load_data(path):
    with open(path) as file:
        return json.load(file)


def load_offer(path):
    offers = load_data(path)

    for offer in offers:
        db.sesion.add(
            Offer(
                id=offer.get("id"),
                order_id=offer.get("order_id"),
                executer_id=offer.get("executor_id")
            )
        )

        db.session.commit()


def load_order(path):
    orders = load_data(path)

    for order in orders:
        db.sesion.add(
            Order(
                **order
            )
        )

        db.session.commit()


def load_user(path):
    users = load_data(path)

    for user in users:
        db.sesion.add(
            User(
                **user
            )
        )

        db.session.commit()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = {'ensure_ancii': False, 'indent': 4}
    app.config['SQLALCHEMY_ECHO'] = True

    with app.context().push():
        db.init_app(app)
        db.drop_all()
        db.create_all()
        offer = load_offer("/HomeWork_2/data/offers.json")
        order = load_order("/HomeWork_2/data/orders.json")
        user = load_user("/HomeWork_2/data/users.json")

    return app


app = create_app()
