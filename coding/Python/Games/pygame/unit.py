import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Grid settings
GRID_SIZE = 50  # Size of each grid cell
GRID_COLOR = (200, 200, 200)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Strategy Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# List to store unit positions
units = []

def draw_grid():
    """Draw the grid on the screen."""
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def draw_units():
    """Draw all units on the grid."""
    for unit in units:
        pygame.draw.rect(screen, BLUE, (unit[0], unit[1], GRID_SIZE, GRID_SIZE))

def main():
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Place a unit on the grid
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x = (mouse_x // GRID_SIZE) * GRID_SIZE
                grid_y = (mouse_y // GRID_SIZE) * GRID_SIZE
                if (grid_x, grid_y) not in units:
                    units.append((grid_x, grid_y))

        # Game logic
        # (Add additional game logic here)

        # Drawing
        screen.fill(WHITE)  # Clear the screen with a white background
        draw_grid()
        draw_units()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()