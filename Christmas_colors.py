import pygame
import time
import math
from random import randint
from pygame import mixer
pygame.init()
mixer.init()
SCREEN_HEIGHT=400
SCREEN_WIDTH=500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#load
tree = pygame.image.load("christmas_tree.jpg").convert_alpha()
w = tree.get_width()
h = tree.get_height()
tree2 = pygame.transform.scale(tree, (math.ceil(w*0.5), math.ceil(h*0.5)))
#varibles
pygame.display.set_caption("Christmas Colors")
mixer.music.load("jingle bell rock.mp3")
mixer.music.set_volume(1)
mixer.music.play()
x = 0
y = 0
treex = 250
treey = 200
sine = 0
colors = [(73,190,44), (44,180,105), (199,43,46), (171,23,23), (255,255,255)]
run = True

#main loop

while run:

    sine += 1

    tree3 = pygame.transform.rotate(tree2, (math.sin(sine)*10))
    tree_rect = tree3.get_rect(center = (treex, treey))
    

    for i in range(2000):
        pygame.draw.rect(screen, (colors[randint(0, (len(colors)-1))]), (x, y, 10, 10))
        y += 10
        if y == 400:
            x += 10
            y = 0
    y = 0
    x = 0
    screen.blit(tree3, tree_rect)

    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()