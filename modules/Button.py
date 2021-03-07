import pygame as pg
import pygame

class Button(object):
    pg.font.init()
    _font_ = pg.font.Font("images/fonts_matrix_cyr.ttf", 36)

    def __init__(self, pos_x, pos_y, name):
        """ Unit """
        self.name = name
        self.font_color = '#047A00'
        self.active = True
        self.focus = False
        self.pressed = False
        self.rect = pg.Rect(pos_x, pos_y, 300, 80)

    def update(self):
        """Обнавление"""
        if self.active:
            self.font_color = '#047A00'
            if self.focus:
                self.font_color = 'Yellow'
                if self.pressed:
                    self.font_color = '#00FF00'
        else:
            self.font_color = 'gray'

    def draw(self, g):
        ''' Отрисовка '''
        pg.draw.rect(g, '#047A00', self.rect, 5)
        self.text_button = self._font_.render(self.name, True, self.font_color)
        self.text_rect = self.text_button.get_rect()
        self.text_rect.center = self.rect.center
        g.blit(self.text_button, self.text_rect)


