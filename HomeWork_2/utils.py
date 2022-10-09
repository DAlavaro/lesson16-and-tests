import json
from data import db


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