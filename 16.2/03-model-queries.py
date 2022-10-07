# Фильтрация выборки
from operator import or_

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc, func
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
    age = db.Column(db.Integer, db.CheckConstraint("age > 18"))
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))

    group = relationship("Group")


class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    users = relationship("User")


db.create_all()

group_01 = Group(id=1, name="Group #1")
group_02 = Group(id=2, name="Group #2")

user_01 = User(id=1, name ="John", age=20, group=group_01)
user_02 = User(id=2, name ="Kate", age=22, group=group_02)
user_03 = User(id=3, name ="Artur", age=23, group=group_01)
user_04 = User(id=4, name ="Maxim", age=24, group=group_01)
user_05 = User(id=5, name ="Lily", age=25, group=group_02)
user_06 = User(id=6, name ="Mary", age=26, group=group_02)

with db.session.begin():
    db.session.add_all([
        user_01,
        user_02,
        user_03,
        user_04,
        user_05,
        user_06,
    ])

"""
SQL -> WHERE
query = User.query.filter(User.name == "Maxim"
"""
query = db.session.query(User).filter(User.name == "Maxim")
# print(f"Запрос {query}")
# print(f"Результат: {query.first().name}")

"""
SQL -> WHERE (Required record)
query = User.query.filter(User.name == "Maxim"
"""
query = db.session.query(User).filter(User.name == "Maxim")
# print(f"Запрос {query}")
# print(f"Результат: {query.one()}")


"""
SQL -> WHERE ... AND
"""

query = db.session.query(User).filter(User.id <=5, User.age > 20)
# print(f"Запрос {query}")
# print(f"Результат: {query.all()}")

"""
SQL -> LIKE
"""
query = db.session.query(User).filter(User.name.like("L%"))
# print(f"Запрос {query}")
# print(f"Результат: {query.all()}")

"""
SQL -> WHERE ... OR ....
"""
query = db.session.query(User).filter(
    or_(User.id <= 5, User.age > 20)
)
# print(f"Запрос {query}")
# print(f"Результат: {query.all()}")

"""
SQL -> WHERE name IS NULL 
"""
query = db.session.query(User).filter(
    User.passport_number == None
)
# print(f"Запрос {query}")
# print(f"Результат: {query.all()}")

"""
SQL -> WHERE name IS  NOT NULL 
"""
query = db.session.query(User).filter(
    User.passport_number != None
)
# print(f"Запрос {query}")
# print(f"Результат: {query.all()}")

"""
SQL -> WHERE ... IN ()
"""
query = db.session.query(User).filter(
    User.id.in_([1, 2])
)
# print(f"Запрос {query}")
# print(f"Результат: {query.all()}")

"""
SQL -> WHERE ... NOT IN ()
"""
query = db.session.query(User).filter(
    User.id.notin_([1, 2])
)
# print(f"Запрос {query}")
# print(f"Результат: {query.all()}")

"""
SQL -> WHERE ... BETWEEN
"""
query = db.session.query(User).filter(
    User.id.between(1, 6)
)
# print(f"Запрос {query}")
# print(f"Результат: {query.all()}")

"""
SQL -> LIMIT
"""
query = db.session.query(User).limit(2)
# print(f"Запрос {query}")
# print(f"Результат: {query.all()}")

"""
SQL -> LIMIT OFFSET
"""
query = db.session.query(User).limit(2).offset(2)
# print(f"Запрос {query}")
# print(f"Результат: {query.all()}")

"""
SQL -> ORDER BY
"""
query = db.session.query(User).order_by(User.id)
# print(f"Запрос {query}")
# print(f"Результат: {query.all()}")
query = db.session.query(User).order_by(desc(User.id))
# print(f"Запрос {query}")
# print(f"Результат: {query.all()}")

"""
SQL -> INNER JOIN
"""
query = db.session.query(User.id, Group.name).join(Group)
print(f"Запрос {query}")
print(f"Результат: {query.all()}")

"""
SQL -> GROUP BY (scalar)
func -> count(user.id)
"""
column = func.count(User.id)
query = db.session.query(column).join(Group).filter(Group.id == 1).group_by(Group.id)
print(f"Запрос {query}")
print(f"Результат: {query.scalar()}")

exit()

if __name__ == '__main__':
    app.run(debug=True)

