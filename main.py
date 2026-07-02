import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TakTanks")

clock = pygame.time.Clock()


running = True

while running:
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()

    screen.fill((30, 30, 30))

    # here i will add all the drawings like the tanks and the ground later

    # here we call the game logic!

    pygame.display.flip()

pygame.quit()
sys.exit()