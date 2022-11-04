from animals import Bear, Cat, Dog, Human, Wolf


def main():
    cat = Cat('Магнат', 4)
    dog = Dog('Лаки', 4)
    bear = Bear('Маша', 2, False)
    wolf = Wolf('Серый', 6)
    human = Human('Paul', 33, 'european')

    print(cat.hunt())
    print(dog.say())
    print(human.work())
    print(bear.awake())
    print(wolf.say())


if __name__ == '__main__':
    main()
