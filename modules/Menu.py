import pygame as pg
from modules.Button import Button

class Menu(object):

    button_name = ['Start', 'Options', 'Loading', 'Safe', 'AddGame', 'Proceed ', '7', 'Exit']

    def __init__(self):
        ''' MENU '''
        self.list_button = []
        for i in range(8):
            pos_x = 300
            pos_y = 100 * i + 50
            if i >= 4:
                pos_x = 650
                pos_y = 100 * i - 350

            button = Button(pos_x, pos_y + 100, self.button_name[i])
            self.list_button.append(button)

    def update(self, e):
        ''' Обнавление '''
        pass

    def draw(self, g):
        ''' Отрисовка '''
        g.fill('black')
        for button in self.list_button:
            button.draw(g)
