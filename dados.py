import json 


def load(arquivo):
    with open(arquivo) as file:
        data = file.read()

    format_data = json.loads(data)

    return format_data

