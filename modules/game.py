import pygame
from modules.Class1 import Class1

local_version = 1
pygame.init()
g = pygame.display.set_mode((800, 600))
pygame.display.set_caption('RATORI')
icon = pygame.image.load('images\\iconPNG.png')
pygame.display.set_icon(icon)
font = pygame.font.SysFont('serif', 32)
msg = 'Инь Янь'
text = font.render(msg, True, 'grey')
game_state = True
class1 = Class1()

image = pygame.image.load('images\\fon.png')
gamemusic = pygame.mixer.music.load('sounds\\S2.mp3')
sound = pygame.mixer.Sound('sounds\\S.mp3')


def game_cycle():
    pygame.mixer.music.play(-1)

    pygame.mixer.Sound.play(sound)
    while game_state:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        class1.draw(g)
        g.blit(text, (350, 50))

        pygame.time.Clock().tick(60)
        pygame.display.update()
