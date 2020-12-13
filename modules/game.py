import pygame

local_version = 1
pygame.init()
g = pygame.display.set_mode((800, 600))
pygame.display.set_caption('RATORI')
icon = pygame.image.load('images\\iconPNG.png')
pygame.display.set_icon(icon)
game_state = True

def game_cycle():
    while game_state:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        g.fill(('white'))

        # pygame.draw.line(g, (255, 255, 100), (50, 50), (500, 100), 1)
        # pygame.draw.aaline(g, (255, 255, 100), (50, 60), (500, 110))
        # pygame.draw.line(g, 'white', (50, 70), (500, 120), 1)
        # pygame.draw.rect(g, 'black', (100, 100, 300, 300), 1)
        # pygame.draw.ellipse(g, 'black', (200, 300, 100, 400), 1)
        # pygame.draw.circle(g, 'white', (400, 400), 100, 1)
        # pygame.draw.arc(g, 'black', (250, 1, 300, 300), -1.57, 1.57, 10)

        pygame.draw.line(g, ('black'), (0, 0), (800, 600), 10)
        pygame.draw.line(g, ('black'), (0,300), (800, 300), 7)
        pygame.draw.line(g, ('black'), (0,600), (800, 0), 10)
        pygame.draw.line(g, ('black'), (400, 600), (400, 0), 7)
        pygame.draw.rect(g, ('black'), (0, 0, 800, 600), 10)

        pygame.time.Clock().tick(60)
        pygame.display.update()
