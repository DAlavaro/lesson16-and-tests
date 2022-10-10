from flask import Blueprint, request, jsonify
from data import db
from models import Order, User

orders_blueprint = Blueprint('orders_blueprint', __name__)


@orders_blueprint.route("/orders", methods=["GET"])
def get_orders():
    """
        Метод GET: Возвращает json файл с всеми заказами
    """
    if request.method == "GET":
        orders_list = Order.query.all()
        orders_response = []
        for order in orders_list:
            orders_response.append({
                "id": order.id,
                "name": order.name,
                "description": order.description,
                "start_date": order.start_date,
                "end_date": order.end_date,
                "address": order.address,
                "price": order.price,
                "customer_id": order.customer_id,
                "executor_id": order.executor_id,
            })
        return jsonify(orders_response)


@orders_blueprint.route("/orders/<int:oid>", methods=["GET"])
def get_order(oid):
    """
        Метод GET: Возвращает заказы по id
    """
    order = Order.query.get(oid)
    if order is None:
        return jsonify("Нет такого заказа")
    return jsonify({
            "id": order.id,
            "name": order.name,
            "description": order.description,
            "start_date": order.start_date,
            "end_date": order.end_date,
            "address": order.address,
            "price": order.price,
            "customer_id": order.customer_id,
            "executor_id": order.executor_id,
             })


@orders_blueprint.route("/orders", methods=["POST"])
def add_order():
    """
        Метод POST: добавляет заказ в таблицу
    """
    order_added = request.json
    new_order = User(**order_added)
    db.session.add(new_order)
    db.session.commit()
    return f'Заказ {order_added["description"]} добавлен'


@orders_blueprint.route("/orders/<int:oid>", methods=["PUT"])
def update_order(oid):
    """
        Метод PUT: добавляет изменения в профиль заказа по id
    """
    recieved_order = request.json
    updated_order = Order.query.get(oid)

    updated_order.name = recieved_order["name"]
    updated_order.description = recieved_order["description"]
    updated_order.start_date = recieved_order["start_date"]
    updated_order.end_date = recieved_order["end_date"]
    updated_order.address = recieved_order["address"]
    updated_order.price = recieved_order["price"]
    updated_order.customer_id = recieved_order["customer_id"]
    updated_order.executor_id = recieved_order["executor_id"]

    db.session.commit()
    return 'Заказ обновлен'


@orders_blueprint.route("/orders/<int:oid>", methods=["DELETE"])
def delete_order(oid):
    """
        Метод DELETE: удаляет пользователя по id
    """
    order_deleted = Order.query.get(oid)
    db.session.delete(order_deleted)
    db.session.commit()
    return f'Заказ {order_deleted.description} удален'
