# отношение один ко многим

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
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))

    group = relationship("Group")


class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    users = relationship("User")


db.create_all()

group_01 = Group(id=1, name="Group #1")
user_01 = User(id=1, name="john", age=30, group=group_01)

with db.session.begin():
    db.session.add(user_01)

user_02 = User(id=2, name="kate", age=31)
group_02 = Group(id=2, name="Group #2", users=[user_02])

with db.session.begin():
    db.session.add(group_02)

user_with_group = User.query.get(2)
print(user_with_group.group.name)

if __name__ == '__main__':
    app.run(debug=True)

