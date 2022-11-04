from abc import ABC, abstractmethod


class Animal(ABC):
    average_lifetime: int

    def __init__(self, name: str, age: int, is_male: bool = True) -> None:
        self._name = name
        self._age = age
        self._is_male = is_male

    @abstractmethod
    def say(self):
        pass

    @abstractmethod
    def hunt(self) -> str:
        return f'{self._name} охотится.'

    def __str__(self) -> str:
        return self._name

    def __repr__(self):
        return f'<\'{self.__class__.__name__}\' object: {self._name}>'

    def to_dict(self):
        result = {"cls": self.__class__.__name__}
        for param in self.__dict__:
            result[param[1:]] = self.__dict__[param]

        return result


class Cat(Animal):
    average_lifetime: int = 17

    def say(self) -> str:
        return f'{self._name} мяучит около миски.'

    def hunt(self) -> str:
        if self._age < 3:
            return f'{self._name} еще котенок - не умеет охотиться!'

        return super().hunt()


class Dog(Animal):
    average_lifetime: int = 12

    def say(self) -> str:
        return f'{self._name} лает на прохожего.'

    def hunt(self) -> str:
        if self._age < 3:
            return f'{self._name} еще щенок - не умеет охотиться!'

        return super().hunt()


class Wolf(Animal):
    average_lifetime: int = 6

    def say(self) -> str:
        return f'{self._name} воет на Луну.'

    def hunt(self) -> str:
        if self._age < 3:
            return f'{self._name} еще волченок - не умеет охотиться!'

        return super().hunt()


class Bear(Animal):
    average_lifetime: int = 25

    def say(self) -> str:
        return f'{self._name} рычит на охотнка.'

    def hunt(self) -> str:
        if self._age < 3:
            return f'{self._name} еще волченок - не умеет охотиться!'

        return super().hunt()

    def sleep(self) -> str:
        return f'{self._name} впадает в зимнюю спячку.'

    def awake(self) -> str:
        if self._is_male:
            return f'{self._name} проснулся слишком рано и стал шатуном!'

        return f'{self._name} проснулась слишком рано и стала шатуном!'


class Human(Animal):
    average_lifetime: int = 74

    def __init__(self, name: str, age: int, nationality: int,
                 is_male: bool = True) -> None:
        super().__init__(name, age, is_male)

        self._nationality = nationality

    def say(self) -> str:
        if self._age < 3:
            return f'{self._name} еще не умеет говорить.'

        return f'{self._name} рассказывает о себе.'

    def hunt(self) -> str:
        return f'{self._name} отказывается охотиться, предпочитая магазин.'

    def work(self) -> str:
        return f'{self._name} трудится на работе.'
