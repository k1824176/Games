import pygame
import time
import math
from random import randint
pygame.init()
pygame.mixer.init()

w=700
h=382

screen = pygame.display.set_mode((w,h))

bg = pygame.image.load("bg.jpg")
chiminey = pygame.image.load("chiminey.png")
spritesheet = pygame.image.load("galloping.png").convert_alpha()
chiminey2 = pygame.transform.rotate(screen, 180)

pygame.mixer.music.load("YO.mp3")
bgx = 0
bgy = 0
bg_width = bg.get_width()

scroll = 0
tiles = math.ceil(w / bg_width)+1
x = 700



def get_image(sheet, width, height):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), (0, 0, width, height))

    return image

frame_0 = get_image(spritesheet, 145, 84)
run = True
pygame.mixer.music.play()


while run:
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, bgy))
    screen.blit(frame_0, (0,0))

    scroll -= 0.08

    if abs(scroll) > bg_width:
        scroll = 0
    screen.blit(chiminey, (x, 382-chiminey.get_height()))
    x -= 0.12

    if x < -(randint(300, 600))-chiminey.get_width():
        x = 700


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()


pygame.quit()