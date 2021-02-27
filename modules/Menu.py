import pygame as pg
from modules.Button import Button

class Menu(object):

    button_name = ['start', '2', '3', '4', '5', '6', '7', 'Выход']

    def __init__(self):
        ''' MENU '''
        self.list_button = []
        for i in range(8):
            button = Button(200, 100, self.button_name[i])
            self.list_button.add(button)

    #Обнавление
    def update(self, e):
        ''' Обнавление '''
        pass

    def draw(self, g):
        ''' Отрисовка '''
        g.fill('yellow')
        for i in self.list_button:
            self.list_button[i].draw(g)
