from abc import ABC


class Animal(ABC):
    pass


class WildAnimal(Animal):
    pass


class Pet(Animal):
    pass


class Cat(Pet):
    pass


class Dog(Pet):
    pass


class Wolf(WildAnimal):
    pass
