from flask import Blueprint, request, jsonify
from data import db
from models import User

users_blueprint = Blueprint('users_blueprint', __name__)

@users_blueprint.route("/users", methods=["GET", "POST"])
def get_users():
    """
    Метод GET: Возвращает json файл с всеми юзерами
    Метод POST: добавляет юзера в таблицу
    """
    if request.method == "GET":
        users_list = User.query.all()

        user_response = []
        for user in users_list:
            user_response.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age,
                "email": user.email,
                "role": user.role,
                "phone": user.phone
            })
        return jsonify(user_response)

    elif request.method == "POST":
        user_added = request.json
        new_user = User(**user_added)
        db.session.add(new_user)
        db.session.commit()
        return f'{user_added["first_name"]} {user_added["last_name"]} added'


@users_blueprint.route("/users/<int:uid>", methods=["GET", "PUT", "DELETE"])
def get_user(uid):
    """
        Метод GET: Возвращает юзера по id
        Метод PUT: добавляет изменения в профиль юзера по id
        Метод DELETE: удаляет пользователя по id
        """

    if request.method == "GET":
        user = User.query.get(uid)
        if user is None:
            return jsonify("Нет такого заказчика")
        return jsonify(({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "age": user.age,
                "email": user.email,
                "role": user.role,
                "phone": user.phone
            }))

    elif request.method == "PUT":
        recieved_user = request.json
        updated_user = User.query.get(uid)

        updated_user.first_name = recieved_user["first_name"]
        updated_user.last_name = recieved_user["last_name"]
        updated_user.age = recieved_user["age"]
        updated_user.email = recieved_user["email"]
        updated_user.role = recieved_user["role"]
        updated_user.phone = recieved_user["phone"]

        db.session.commit()
        return f'{updated_user.first_name} {updated_user.last_name} обновлен'

    elif request.method == "DELETE":
        user_deleted = User.query.get(uid)
        db.session.delete(user_deleted)
        db.session.commit()
        return f'{user_deleted.first_name} {user_deleted.last_name} удален'