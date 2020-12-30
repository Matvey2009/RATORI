import pygame as pg

class Button(object):
    pg.init()
    _image_ = pg.image.load('images\\button.png')

    # Unit
    def __init__(self):
        self.image = self._image_
        self.rect = self.image.get_rect()

    # Отрисовка
    def draw(self, g):
        g.blit(self.image, self.rect)
