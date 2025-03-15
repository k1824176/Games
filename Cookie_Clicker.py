import pygame
from random import randint
import math
import time
pygame.init()

#set up the screen
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cookie Clicker")

#image loading dock
cookie = pygame.image.load("cookie.png").convert_alpha()
#variables
sinx = 1
x = 500
y = 300
run=True
text_font = pygame.font.SysFont("Comic Sans", 80)
score = 0
big_scale = 1.1
clicked = False
#def functions
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))
while run:
    sinx += 0.08
    cookie2 = pygame.transform.rotate(cookie, math.sin(sinx)*40)
    h = cookie2.get_height()
    w = cookie2.get_width()
    biggcookie = pygame.transform.scale(cookie2, (math.ceil(h*big_scale), math.ceil(w*big_scale)))
    cookie_rect = cookie2.get_rect(center = (x, y))
    biggcookie_rect = biggcookie.get_rect(center = (x,y))

    screen.fill((244,164,96))

    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if cookie_rect.collidepoint(pos):
        screen.blit(biggcookie, biggcookie_rect)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if clicked == False:
                score += 1
            clicked = True
            big_scale = 0.9
        if event.type == pygame.MOUSEBUTTONUP:
            big_scale = 1.1
            clicked = False
    else:

    #bliting and drawing space
        screen.blit(cookie2, cookie_rect)
    draw_text("Score: "+str(score), text_font, (0,0,0), 350, 20 )

    time.sleep(0.01)
    #update the screen
    pygame.display.update()

pygame.quit()