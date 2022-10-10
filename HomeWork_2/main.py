# Импорт библиотек

from models import User, Order, Offer
from utils import get_table
from create_app import create_app
from views_user import users_blueprint
from views_orders import orders_blueprint
from views_offers import offers_blueprint


app = create_app()

# Регистрация блюпринтов
app.register_blueprint(users_blueprint)
app.register_blueprint(orders_blueprint)
app.register_blueprint(offers_blueprint)

# Заполнение таблиц
get_table(User, "data/users.json")
get_table(Order, "data/orders.json")
get_table(Offer, "data/offers.json")

if __name__ == "__main__":
    app.run()
