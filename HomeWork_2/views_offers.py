from flask import Blueprint, request, jsonify
from data import db
from models import Offer

offers_blueprint = Blueprint('offers_blueprint', __name__)


@offers_blueprint.route("/offers", methods=["GET"])
def get_offers():
    """
        Метод GET: Возвращает json файл с всеми предложениями
    """
    offers_list = Offer.query.all()

    offers_response = []
    for offer in offers_list:
        offers_response.append({
            "id": offer.id,
            "order_id": offer.id,
            "executor_id": offer.executor_id,
                })
    return jsonify(offers_response)


@offers_blueprint.route("/offers/<int:ofid>", methods=["GET"])
def get_offer(ofid):
    """
        Метод GET: Возвращает предложения  по  id
    """
    offer = Offer.query.get(ofid)
    if offer is None:
        return jsonify("Нет такого заказа")
    return jsonify({
            "id": offer.id,
            "order_id": offer.id,
            "executor_id": offer.executor_id,
            })


@offers_blueprint.route("/offers", methods=["POST"])
def add_offer():
    """
        Метод POST: добавляет заказ в таблицу
    """
    offer_added = request.json
    new_offer = Offer(**offer_added)
    db.session.add(new_offer)
    db.session.commit()
    return 'Предложение добавлено'


@offers_blueprint.route("/offers/<int:ofid>", methods=["PUT"])
def update_offer(ofid):
    """
        Метод PUT: добавляет изменения в профиль предложения по id
    """
    recieved_offer = request.json
    updated_offer = Offer.query.get(ofid)

    updated_offer.order_id = recieved_offer["order_id"]
    updated_offer.executor_id = recieved_offer["executor_id"]

    db.session.commit()
    return 'Предложение обновлено'


@offers_blueprint.route("/offers/<int:ofid>", methods=["DELETE"])
def delete_offer(ofid):
    """
        Метод DELETE: удаляет пользователя по id
    """
    offer_deleted = Offer.query.get(ofid)
    db.session.delete(offer_deleted)
    db.session.commit()
    return 'Предложение  удалено'