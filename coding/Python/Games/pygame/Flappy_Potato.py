import pygame
import time

pygame.init()


screen = pygame.display.set_mode((600,400))

#Load the potato
potato = pygame.image.load(r"C:\Users\hfeng\Desktop\Albert\coding\Python\Images\potato.gif")

#variables
potatoX = 300
potatoY = 200
gravity = 1


run = True
while run:

    screen.fill((86, 191, 91))
    screen.blit(potato, (potatoX, potatoY))
    
    gravity += 1
    potatoY += gravity


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0] == True:
            gravity = 1
            potatoY -= 3
    pygame.display.update()
pygame.quit()