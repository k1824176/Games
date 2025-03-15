import pygame
import time
from random import randint
pygame.init()
SCREEN_HEIGHT=400
SCREEN_WIDTH=500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Autumn Colors")
x = 0
y = 0
colors = [(252,210,56), (245,168,0), (241,132,7), (219,84,0), (177,32,0), (184,43,43), (221,113,22), (238,168,62),]
run = True
while run:
    for i in range(2000):
        pygame.draw.rect(screen, (colors[randint(0, (len(colors)-1))]), (x, y, 10, 10))
        y += 10
        if y == 400:
            x += 10
            y = 0
    y = 0
    x = 0
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()