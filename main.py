from random import randint

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    # Новая константа.
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'

    def __init__(self, name):
        self.name = name

    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"')

    # Новый метод базового класса.
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'
    ...


class Warrior(Character):
    ...


class Mage(Character):
    ...


class Healer(Character):
    ...
