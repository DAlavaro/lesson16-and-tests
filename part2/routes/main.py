# УРОК 16 Задание 8
# В этом финальном задании вам нужно
# применить знания о моделях для создания 3 представлений,
# которые реализуют запросы на создание, добавление, удаление.

"""
    # Задание
    # Шаг 1.
    # ######
    # Создайте представение для эндпоинта GET /guides
    # которое возвращает список всех гидов со всеми полями
    # в формате JSON
    #
    #
    # Шаг 2.
    # ######
    # - Создайте представение для эндпоинта GET /guides/{id}
    # которое возвращает одного гида со всеми полями
    # в формате JSON в соответствии с его id
    #
    # Шаг 3.
    # ######
    # Создайте представение для эндпоинта
    # GET /guides/{id}/delete`, которое удаляет
    # одного гида в соответствии с его `id`
    #
    # Шаг 4.
    # ######
    # Создайте представление для эндпоинта POST /guides
    #  которое добавляет в базу данных гида, при получении
    # следующих данных:
    # {
    #     "surname": "Иванов",
    #     "full_name": "Иван Иванов",
    #     "tours_count": 7,
    #     "bio": "Провожу экскурсии",
    #     "is_pro": true,
    #     "company": "Удивительные экскурсии"
    # }
    # Шаг 5.
    # ######
    # - Допишите представление из шага 1 для фильтрации так,
    # чтобы при получении запроса типа /guides?tours_count=1
    # возвращались гиды с нужным количеством туров.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from guides_sql import CREATE_TABLE, INSERT_VALUES

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
db = SQLAlchemy(app)
with db.session.begin():
    db.session.execute(text(CREATE_TABLE))
    db.session.execute(text(INSERT_VALUES))


class Guide(db.Model):
    __tablename__ = 'guide'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String)
    full_name = db.Column(db.String)
    tours_count = db.Column(db.Integer)
    bio = db.Column(db.String)
    is_pro = db.Column(db.Boolean)
    company = db.Column(db.Integer)

def guide_func(instance):
    return {
        "id": instance.id,
        "surname": instance.surname,
        "full_name": instance.full_name,
        "tours_count": instance.tours_count,
        "bio": instance.bio,
        "is_pro": instance.is_pro,
        "company": instance.company,
    }


@app.route("/guides")
def get_all_and_by_tours_count():
    tours_count = request.args.get("tours_count")
    result = []
    if not tours_count:
        guides = Guide.query.all()
        for guide in guides:
            result.append(guide_func(guide))
        return jsonify(result)
    guides = Guide.query.filter_by(tours_count=tours_count)
    for guide in guides:
        result.append(guide_func(guide))
    return jsonify(result)

@app.get("/guides/<int:gid>")
def get_one(gid):
    giude = Guide.query.get(gid)
    return jsonify(guide_func(giude))

@app.route("/guides/<int:gid>/delete")
def delete_guide(gid):
    guide = Guide.query.get(gid)
    db.session.delete(guide)
    db.session.commit()
    return jsonify("")

@app.post("/guides")
def create_guide():
    data = request.json
    guide = Guide(
        surname = data.get("surname"),
        full_name = data.get("full_name"),
        tours_count = data.get("tours_count"),
        bio = data.get("bio"),
        is_pro = data.get("is_pro"),
        company = data.get("company"),
    )
    db.session.add(guide)
    db.session.commit()
    return jsonify(guide_func(guide))




if __name__ == "__main__":
    app.run()
