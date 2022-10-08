import json

from __init__ import db
from models import Offer, Order, User


def load_data(path):
    with open(path) as file:
        return json.load()

def load_offer(path):
    offers = load_data()

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
    orders = load_data()

    for order in orders:

        db.sesion.add(
            Order(
                **order
            )
        )

        db.session.commit()


def load_user(path):
    orders = load_data()

    for user in users:

        db.sesion.add(
            User(
                **user
            )
        )

        db.session.commit()

