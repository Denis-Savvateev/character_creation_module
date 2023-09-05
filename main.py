"""This is the main module of game."""

from random import randint

from graphic_arts.start_game_banner import run_screensaver


class Chsrscter():
    def __init__(self, name):
        self.name = name

    def attack(self):
        return (f'{self.name} нанёс урон противнику '
                f'равный {5 + randint(3, 5)}')
