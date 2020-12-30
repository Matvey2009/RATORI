import pygame as pg
from modules.Unit import Unit

class Game(object):

    # GAME
    def __init__(self):
        self.unit = Unit()

    #Обнавление
    def update(self, e):
        if e.type == pg.KEYDOWN and e.key == pg.K_UP:
            self.unit.rect.y -= 3
        if e.type == pg.KEYDOWN and e.key == pg.K_DOWN:
            self.unit.rect.y += 3
        if e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
            self.unit.rect.x += 3
    # Отрисовка
    def draw(self, g):
        g.fill('grey')
        self.unit.draw(g)