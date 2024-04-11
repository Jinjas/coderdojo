import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,500))
pygame.display.set_caption('hello world!')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT()
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('esquerda')
            if event.key == pygame.K_RIGHT:
                print('direita')
        pygame.draw.rect(DISPLAYSURF, (0, 255, 255), pygame.Rect(50,50,300,400))
        pygame.draw.rect(DISPLAYSURF, (0, 0,0), pygame.Rect(75,75,250,350))

    pygame.display.update()


