import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from HomeWork_2.models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)


# Создание модели user
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    role = db.Column(db.String)
    phone = db.Column(db.String)

# Создание модели order
class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    start_date = db.Column(db.String)
    end_date = db.Column(db.String)
    address = db.Column(db.String)
    price = db.Column(db.String)

    customer_id = db.Column(db.Integer, db.ForeignKey(f"{User.__tablename__}.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey(f"{User.__tablename__}.id"))

    customer = db.relationship("User", foreign_keys=[customer_id])
    executor = db.relationship("User", foreign_keys=[executor_id])

db.drop_all()
db.create_all()


def get_table(cls, filename):
    """
        Преобразует json файл и заполняет таблицу
        :param cls:
        :param filename:
        """
    with open(filename, "r", encoding='UTF-8') as file:
        json_list = json.load(file)

        for element in json_list:
            table_element = cls(**element)
            db.session.add(table_element)
        db.session.commit()

    db.create_all()

print(get_table(User, "data/users.json"))