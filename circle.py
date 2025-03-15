import pygame
from random import randint
import time

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circle Generator")

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

# Set up colors
colors = [
    (135, 206, 235),  # Sky Blue
    (144, 238, 144),  # Light Green
    (255, 127, 80),   # Coral
    (147, 112, 219),  # Medium Purple
    (64, 224, 208),   # Turquoise
    (255, 215, 0),    # Gold
    (250, 128, 114),  # Salmon
    (255, 20, 147),   # Deep Pink
    (32, 178, 170),   # Light Sea Green
    (106, 90, 205)    # Slate Blue
]

# List to store circles
circles = []

# Main game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Randomize the values for a new circle
    circle_radius = randint(10, 40)
    circle_color = colors[randint(0, len(colors) - 1)]
    x = randint(circle_radius, screen_width - circle_radius)
    y = randint(circle_radius, screen_height - circle_radius)

    # Add the new circle to the list
    circles.append((circle_color, (x, y), circle_radius))

    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 0))  # Black

    # Draw all circles
    for circle in circles:
        pygame.draw.circle(screen, circle[0], circle[1], circle[2])


    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()