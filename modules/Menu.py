import pygame as pg
from modules.Button import Button

class Menu(object):

    button_name = ['START', 'OPTIONS', 'LOADING', 'SAFE', 'ADDGAME', 'PROCEED ', '0110101011', 'EXIT']

    def __init__(self):
        """ Menu """
        self.list_button = []
        for i in range(8):
            pos_x = 300
            pos_y = 100 * i + 50
            if i >= 4:
                pos_x = 650
                pos_y = 100 * i - 350
            button = Button(pos_x, pos_y + 100, self.button_name[i])
            self.list_button.append(button)
        self.button_action = None
        self.list_button[6].active = False



    def update(self, e):
        """ Обнавление """
        if e.type == pg.MOUSEMOTION:
            self.button_action = None
        pos = pg.mouse.get_pos()
        click = pg.mouse.get_pressed(3)
        for button in self.list_button:
            if button.active and button.rect.collidepoint(pos):
                button.focus = True
                if click[0]:
                    button.pressed = True
                    self.functions(button.name)
                else:
                    button.pressed = False
            else:
                button.focus = False
            button.update()

    def draw(self, g):
        """ Отрисовка """
        g.fill('black')
        for button in self.list_button:
            button.draw(g)
    def function (self, button_name):
        pass
