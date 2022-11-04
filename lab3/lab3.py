import json
import os
from datetime import datetime

from animals import Bear, Cat, Dog, Human, Wolf


def write_json(data, path=None):
    if path is None:
        path = os.path.dirname(os.path.abspath(__file__)) + '/info_write.json'

    if isinstance(data, str):
        data = json.loads(data)

    with open(file=path, mode='w', encoding='utf-8') as file:
        json.dump(obj=data, fp=file, ensure_ascii=False, indent=4)


def main():
    cat = Cat('Магнат', 4)
    dog = Dog('Лаки', 4)
    bear = Bear('Маша', 2, False)
    wolf = Wolf('Серый', 6)
    human = Human('Paul', 33, 'американец')

    objects = [cat, dog, bear, wolf, human, ]

    data = {
        'upload': str(datetime.today()),
        'animals': []
    }

    for obj in objects:
        data['animals'].append(obj.to_json_dict())

    write_json(data)


if __name__ == '__main__':
    main()
