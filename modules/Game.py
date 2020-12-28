import pygame as pg
from modules.Unit import Unit

class Game(object):

    # GAME
    def __init__(self):
        self.unit = Unit()

    # Отрисовка
    def draw(self, g):
        g.fill('grey')
        self.unit.draw(g)