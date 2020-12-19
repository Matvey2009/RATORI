import pygame

class Class1(object):
    def draw(self, g):
        g.fill('white')

        # pygame.draw.line(g, (255, 255, 100), (50, 50), (500, 100), 1)
        # pygame.draw.aaline(g, (255, 255, 100), (50, 60), (500, 110))
        # pygame.draw.line(g, 'white', (50, 70), (500, 120), 1)
        # pygame.draw.rect(g, 'black', (100, 100, 300, 300), 1)
        # pygame.draw.ellipse(g, 'black', (200, 300, 100, 400), 1)
        # pygame.draw.circle(g, 'white', (400, 400), 100, 1)
        # pygame.draw.arc(g, 'black', (250, 1, 300, 300), -1.57, 1.57, 10)
        # g.blit(image, (0, 0))

        # pygame.draw.lines(g, 'black', (100, 100), (200, 200), (100, 200), 5) /|\
        # pygame.draw.polygon(g, 'black', ((100, 200), (200, 200), (200, 300), (300, 300), (300, 400)), 0)

        pygame.draw.rect(g, ('black'), (0, 0, 800, 600), 10)

