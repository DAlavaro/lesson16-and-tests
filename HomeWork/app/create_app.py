from flask import Flask

from __init__ import db
from utils import load_data, load_offer, load_order, load_user

from flask_sqlalchemy import SQLAlchemy





def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = {'ensure_ancii': False, 'indent': 4}
    app.config['SQLALCHEMY_ECHO'] = True

    with app.context():
        db.init_app(app)
        db.create_all()
        offer = load_offer("/Volumes/APPLE HDD/SKYPRO/lesson16-and-tests/HomeWork/data/offers.json")
        order = load_order("/Volumes/APPLE HDD/SKYPRO/lesson16-and-tests/HomeWork/data/orders.json")
        user = load_user("/Volumes/APPLE HDD/SKYPRO/lesson16-and-tests/HomeWork/data/users.json")

    return app
