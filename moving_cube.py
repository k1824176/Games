import pygame
from math import cos, sin, radians, degrees

pygame.init()

SCREEN_HEIGHT=400
SCREEN_WIDTH=500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#set the rect
rect_width = 20
rect_height = 20
rect_col = (230, 230, 250)
rect_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
rect_surface.fill(rect_col)
angle = 0
rect = rect_surface.get_rect(center = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
delta_x = 0
delta_y = 0
run = True
speed = 2

#dir
line_color = (255, 0, 0)  # Red color for the line
line_start = (rect_width // 2, rect_height // 2)
line_end = (rect_width, rect_height // 2)
pygame.draw.line(rect_surface, line_color, line_start, line_end, 2)
#FPS
clock = pygame.time.Clock()
#main loop

while run:
    screen.fill((0,0,0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        angle -= 2
    if keys[pygame.K_RIGHT]:
        angle += 2
    if keys[pygame.K_UP]:
        rad_angle = radians(angle)
        delta_x=cos(rad_angle)*speed
        delta_y=sin(rad_angle)*speed
        rect = rect.move(delta_x, delta_y)
    
    rotated_rect_surface = pygame.transform.rotate(rect_surface, -angle)
    rotated_rect = rotated_rect_surface.get_rect(center = rect.center)
    
    screen.blit(rotated_rect_surface, rotated_rect.topleft)

    pygame.display.update()
    clock.tick(60)
pygame.quit()