import pygame as pg
import pygame

class Button(object):
    pg.font.init()
    _font_ = pg.font.SysFont("cambria", 42)

    def __init__(self, pos_x, pos_y, name):
        ''' Unit '''
        self.name = name
        self.active = True
        self.focus = False
        self.pressed = False
        self.rect = pg.Rect(pos_x, pos_y, 300, 80)

    def draw(self, g):
        ''' Отрисовка '''
        pg.draw.rect(g, 'black', self.rect, 5)
        self.text_button = self._font_.render(self.name, True, 'blue')
        self.text_rect = self.text_button.get_rect()
        self.text_rect.center = self.rect.center
        g.blit(self.text_button, self.text_rect)
