import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

#window icon
icon = pygame.image.load("tetris-logo.png")
pygame.display.set_icon(icon)

# Main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))  # Black

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()