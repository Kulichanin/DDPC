from json import load


def read_json_file(name_dile: str) -> dict:
    with open(name_dile) as json_file:
        return load(json_file)
