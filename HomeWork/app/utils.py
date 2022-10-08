import json


def load_data(path):
    with open(path) as file:
        return json.load()

def load_offer(path):
    offer = load_data()

