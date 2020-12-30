import pygame as pg
from modules.Button import Button

class Menu(object):

    # MENU
    def __init__(self):
        self.button = Button()

    #Обнавление
    def update(self, e):
        pass

    # Отрисовка
    def draw(self, g):
        g.fill('yellow')
        self.button.draw(g)
