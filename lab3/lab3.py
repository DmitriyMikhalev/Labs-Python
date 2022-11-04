import sys
from datetime import datetime

from animals import Bear, Cat, Dog, Human, Wolf
from json_functions import read_json, valid_data, write_json


def str_to_class(classname: str):
    return getattr(sys.modules[__name__], classname)


def main() -> None:
    cat = Cat(name='Магнат', age=4)
    dog = Dog(name='Лаки', age=4)
    bear = Bear(name='Маша', age=2, is_male=False)
    wolf = Wolf(name='Серый', age=6)
    human = Human(name='Paul', age=33, nationality='американец')

    objects = [cat, dog, bear, wolf, human, ]
    data = {
        'upload': str(datetime.today()),
        'animals': [],
    }
    for obj in objects:
        data['animals'].append(obj.to_dict())

    write_json(data)

    objects.clear()
    data = read_json()
    if valid_data(data):
        for obj in data['animals']:
            klass = str_to_class(obj.pop('cls'))
            objects.append(klass(**obj))

        with open('output_read.txt', 'w', encoding='utf-8') as file:
            output = ', '.join(str(obj) for obj in objects)
            file.write(output)


if __name__ == '__main__':
    main()
