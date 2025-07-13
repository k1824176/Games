import pygame
import time
import random

pygame.init()

#screen
screen_width = 600
screen_height = 600
background = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Falling Banana')


#load imgs
banana = pygame.image.load('bana.png')


#things
w = banana.get_width()
h = banana.get_height()
scale = 0.05
angle = 0
small_banana = pygame.transform.scale(banana, (int(w * scale), int(h * scale)))
font = pygame.font.SysFont("arialblack", 60)

#vars

x = screen_width // 2
y = 100
crate_x = 230
crate_y = 600
crate_width = 300
crate_height = 50
width = 30
height = 30
vel = 0.5
Text_col = (172, 120, 186)
Score = 0

changex = random.randint(25, 370)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    background.blit(img, (x, y))

    


# main gme loop

run = True
while run:

    


    angle += 0.4
    
    crate = pygame.Rect(crate_x, crate_y, crate_width, crate_height)

    background.fill((251,198,207))

    draw_text(f"Score:"+str(Score), font, Text_col, 230, 400)

    
    copy_img = pygame.transform.rotate(small_banana, angle)
    obstacle = copy_img.get_rect(center=(x, y))
    background.blit(copy_img, obstacle)
                
    crate_y += -0.3


    if crate_y <= 10:
        crate_y = 580
        changex = random.randint(0, 600)
        Score += 1

    
        
        


                

    crate_x = changex



    #event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel

    if x <= 10:
        x = 10

    if x >= 570:
        x = 570


    pygame.draw.rect(background, (92, 64, 51), crate)
        
    if crate.colliderect(obstacle):
        background.fill((1, 203, 174))
        draw_text("You Died", font, Text_col, 150, 150)
        run = False
    pygame.display.update()
time.sleep(0.5)
pygame.quit()