import json

def load_json(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data