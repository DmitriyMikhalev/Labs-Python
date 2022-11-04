import json
import os

def read_json(path: str = None) -> dict:
    if path is None:
        path = os.path.dirname(os.path.abspath(__file__)) + '/info_read.json'

    with open(file=path, mode='r', encoding='utf-8') as file:
        return json.load(fp=file)


def valid_data(data: dict) -> bool:
    if not isinstance(data, dict):
        return False

    if not all(key in data for key in ('upload', 'animals')):
        return False

    if not isinstance(data['animals'], list):
        return False

    if not all(isinstance(obj, dict) for obj in data['animals']):
        return False

    if not all('cls' in obj.keys() for obj in data['animals']):
        return False

    return True


def write_json(data: dict, path: str = None) -> None:
    if path is None:
        path = os.path.dirname(os.path.abspath(__file__)) + '/info_write.json'

    if isinstance(data, str):
        data = json.loads(data)

    with open(file=path, mode='w', encoding='utf-8') as file:
        json.dump(obj=data, fp=file, ensure_ascii=False, indent=4)