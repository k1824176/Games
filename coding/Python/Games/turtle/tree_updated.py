import pygame
import sys
import random
import turtle

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tree")

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

# Main game loop
run = True
while run:

    screen.fill((174, 198, 207))

    pygame.draw.rect(screen, (119, 221, 119), (0, 500, 800, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()