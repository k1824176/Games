import pygame
pygame.init()


screen = pygame.display.set_mode((600,400))


run = True
while run:

    screen.fill((86, 191, 91))

    pygame.draw.rect(screen, (255, 127, 127), (200,100, 40, 40),)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
                
    pygame.display.update()
pygame.quit()