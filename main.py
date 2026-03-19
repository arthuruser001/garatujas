import pygame

pygame.init()

screeen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screeen.fill('red')

    pygame.display.flip()

    clock.tick(60)