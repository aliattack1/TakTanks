import pygame
import sys

from generation import status

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
    for index, point in enumerate(status['ground']):
        if index == 10:
            break
        pygame.draw.line(screen, (0, 255, 0), (index*80, point+400), ((index+1)*80, status['ground'][index+1]+400), 4)

    pygame.display.flip()

pygame.quit()
sys.exit()