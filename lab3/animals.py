from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class provides create an object Animal.
    Required params:
        name: str
        age: int

    Attributes:
        average_lifetime: int
        name: str
        age: int
        is_male: bool
    """
    average_lifetime: int

    def __init__(self, name: str, age: int, is_male: bool = True) -> None:
        self._name = name
        self._age = age
        self._is_male = is_male

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f'<\'{self.__class__.__name__}\' object: {self._name}>'

    @abstractmethod
    def hunt(self) -> str:
        return f'{self._name} охотится.'

    @abstractmethod
    def say(self) -> str:
        pass

    def to_dict(self) -> dict:
        result = {"cls": self.__class__.__name__}
        for param in self.__dict__:
            result[param[1:]] = self.__dict__[param]

        return result


class Cat(Animal):
    average_lifetime: int = 17

    def hunt(self) -> str:
        if self._age < 3:
            return f'{self._name} еще котенок - не умеет охотиться!'

        return super().hunt()

    def say(self) -> str:
        return f'{self._name} мяучит около миски.'


class Dog(Animal):
    average_lifetime: int = 12

    def hunt(self) -> str:
        if self._age < 3:
            return f'{self._name} еще щенок - не умеет охотиться!'

        return super().hunt()

    def say(self) -> str:
        return f'{self._name} лает на прохожего.'


class Wolf(Animal):
    average_lifetime: int = 6

    def hunt(self) -> str:
        if self._age < 3:
            return f'{self._name} еще волченок - не умеет охотиться!'

        return super().hunt()

    def say(self) -> str:
        return f'{self._name} воет на Луну.'


class Bear(Animal):
    average_lifetime: int = 25

    def awake(self) -> str:
        if self._is_male:
            return f'{self._name} проснулся слишком рано и стал шатуном!'

        return f'{self._name} проснулась слишком рано и стала шатуном!'

    def hunt(self) -> str:
        if self._age < 3:
            return f'{self._name} еще волченок - не умеет охотиться!'

        return super().hunt()

    def say(self) -> str:
        return f'{self._name} рычит на охотнка.'

    def sleep(self) -> str:
        return f'{self._name} впадает в зимнюю спячку.'


class Human(Animal):
    average_lifetime: int = 74

    def __init__(self, name: str, age: int, nationality: int,
                 is_male: bool = True) -> None:
        super().__init__(name, age, is_male)

        self._nationality = nationality

    def hunt(self) -> str:
        return f'{self._name} отказывается охотиться, предпочитая магазин.'

    def say(self) -> str:
        if self._age < 3:
            return f'{self._name} еще не умеет говорить.'

        return f'{self._name} рассказывает о себе.'

    def work(self) -> str:
        return f'{self._name} трудится на работе.'
