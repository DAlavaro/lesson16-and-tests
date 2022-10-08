from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import load_data

db = SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = {'ensure_ancii': False, 'indent': 4}

    with app.context():
        db.init_app(app)
        db.create_all()
        offer = load_data("/Volumes/APPLE HDD/SKYPRO/lesson16-and-tests/HomeWork/data/offers.json")
