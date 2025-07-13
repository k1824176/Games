import pygame
from random import randint

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Birb")
birb = pygame.image.load("birb.jpg")



# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:

    #birb coordinates
    birbx = randint(0, SCREEN_WIDTH)
    birby = randint(0, SCREEN_HEIGHT)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

    #Draw the birb
    screen.blit(birb, (0, 0))

pygame.quit()