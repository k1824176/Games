import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rotating Donut")
font = pygame.font.SysFont('Arial', 10, bold=True)

# Starting position
x_start, y_start = 0, 0

x_separator = 10
y_separator = 10

rows = screen_height // y_separator
cols = screen_width // x_separator
screen_size = rows * cols

x_offset = cols / 2
y_offset = rows / 2

A, B = 0, 0

theta_spacing = 5
phi_spacing = 5

illumination = ".,-~:;=!*#$@"

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

def text_display(letter, x_start, y_start):
    text = font.render(str(letter), True, (174, 198, 207))  # Donut color
    screen.blit(text, (x_start, y_start))

# Main game loop
run = True
while run:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Our code
    z = [0] * screen_size
    b = [' '] * screen_size

    for i in range(0, 628, theta_spacing):
        for j in range(0, 628, phi_spacing):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 30 * D * (l * h * m - t * n))
            y = int(y_offset + 15 * D * (l * h * n + t * m))
            o = int(x + cols * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if rows > y > 0 and cols > x > 0 and D > z[o]:
                z[o] = D
                b[o] = illumination[N if N > 0 else 0]

    if y_start == rows * y_separator - y_separator:
        y_start = 0

    for i in range(len(b)):
        if i == 0 or i % cols:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator

    A += 0.04
    B += 0.02

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()