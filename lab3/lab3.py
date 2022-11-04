import sys
from datetime import datetime

from animals import Bear, Cat, Dog, Human, Wolf
from json_functions import read_json, valid_data, write_json


def main() -> None:
    bear = Bear(age=2, is_male=False, name='Маша')
    cat = Cat(age=4, name='Магнат')
    dog = Dog(age=4, name='Лаки')
    human = Human(age=33, name='Paul', nationality='американец')
    wolf = Wolf(age=6, name='Серый')

    objects = [bear, cat, dog, human, wolf, ]
    data = {
        'upload': str(datetime.today()),
        'animals': [],
    }
    for obj in objects:
        data['animals'].append(obj.to_dict())

    write_json(data)

    objects.clear()
    data: dict = read_json()
    if valid_data(data):
        for obj in data['animals']:
            klass = str_to_class(obj.pop('cls'))
            objects.append(klass(**obj))

        with open(encoding='utf-8', file='output_read.txt', mode='w') as file:
            output = ', '.join(str(obj) for obj in objects)
            file.write(output)


def str_to_class(classname: str):
    return getattr(sys.modules[__name__], classname)


if __name__ == '__main__':
    main()
