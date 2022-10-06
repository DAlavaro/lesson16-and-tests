# Ограничения

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

# Установка инструментария
# pip3 install Flask sqlalchemy flask-sqlalchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    passport_number =db.Column(db.String(3), unique=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, db.CheckConstraint("age >18"))
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))

    group = relationship("Group")


class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    users = relationship("User")


db.create_all()

try:
    user_01 = User(id=1, name="john", age=30, passport_number="123")

    with db.session.begin():
        db.session.add(user_01)

    user_01_copy = User(name="john", age=30, passport_number="456")

    with db.session.begin():
        db.session.add(user_01_copy)

except Exception as e:
    print(e)

try:
    user_02 = User(id=2, name="Kate", age=30, passport_number="000")

    with db.session.begin():
        db.session.add(user_02)
except Exception as e:
    print(e)
exit()


try:
    user_03 = User(id=3, name="Kate", age=15, passport_number="001")

    with db.session.begin():
        db.session.add(user_03)
except Exception as e:
    print(e)
exit()

if __name__ == '__main__':
    app.run(debug=True)

