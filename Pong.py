import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pong")

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

#set up paddles
paddle_width = 10
paddle_height = 100
paddle_color = (255, 255, 255)
paddle_speed = 5
paddle1_y =250
paddle2_y = 250

#set up ball
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_width = 10
ball_height = 10
ball_color = (255, 255, 255)
ball_speed_x = 5
ball_speed_y = 5


score1 = 0
score2 = 0
# Main game loop
running = True

while running:

    screen.fill((0, 0, 0))
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < screen_height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < screen_height - paddle_height:
        paddle2_y += paddle_speed
        

    pygame.draw.rect(screen, paddle_color, (0,paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, paddle_color, (screen_width - paddle_width, paddle2_y, paddle_width, paddle_height))

    #ball movment
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    #tob adn bottom collision
    if ball_y <= 0 or ball_y >= screen_height - ball_height:
        ball_speed_y = -ball_speed_y
    if ball_x <= 0 or ball_x >= screen_width - ball_width:
        ball_speed_x = -ball_speed_x

    #ball with paddle collision
    if ball_x <= paddle_width and paddle1_y < ball_y + ball_height and paddle1_y + paddle_height > ball_y:
        ball_speed_x = -ball_speed_x
    if ball_x >= screen_width - paddle_width - ball_width and paddle2_y < ball_y + ball_height and paddle2_y + paddle_height > ball_y:
        ball_speed_x = -ball_speed_x

    #ball out of bounds
    if ball_x <= 0:
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        score2 += 1
        
    if ball_x >= screen_width - ball_width:
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        score1 += 1
        

    if score1 == 5:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        text = font.render("Player 1 wins!", True, (255, 255, 255))
        screen.blit(text, (screen_width // 2 - 100, screen_height // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
    else:
        if score2 == 5:
            screen.fill((0, 0, 0))
            font = pygame.font.Font(None, 36)
            text = font.render("Player 2 wins!", True, (255, 255, 255))
            screen.blit(text, (screen_width // 2 - 100, screen_height // 2))
            pygame.display.flip()
    
    pygame.draw.rect(screen, ball_color, (ball_x, ball_y, ball_width, ball_height))
    font = pygame.font.Font(None, 36)
    
    score1_text = font.render(str(score1), True, (255, 255, 255))
    score2_text = font.render(str(score2), True, (255, 255, 255))
    screen.blit(score1_text, (screen_width // 4, 50))
    screen.blit(score2_text, (3 * screen_width // 4, 50))
    # Update the display
    pygame.display.flip()
    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()