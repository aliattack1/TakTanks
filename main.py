import pygame
import sys
from generation import status
pygame.init()
WIDTH, HEIGHT = 800, 700
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

    # ground
    pygame.draw.polygon(screen, (80, 160, 60), status['ground']+[(800, 600), (0, 600)])

    pygame.draw.rect(screen, (200, 180, 200), (100, 400, 60, 20))
    pygame.draw.rect(screen, (200, 180, 200), (640, 400, 60, 20))

    # here we call the game logic!

    pygame.display.flip()
pygame.quit()
sys.exit()