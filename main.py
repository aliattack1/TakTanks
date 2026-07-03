import pygame
import sys
from generation import status
import tank
pygame.init()
WIDTH, HEIGHT = 800, 700
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TakTanks")
clock = pygame.time.Clock()
running = True
tank1 = tank.Tank(100, 400)
tank2 = tank.Tank(640, 400)

allsprites = pygame.sprite.Group()
allsprites.add(tank1)
allsprites.add(tank2)

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    screen.fill((255,255,255))
    # here i will add all the drawings like the tanks and the ground later

    # ground
    pygame.draw.polygon(screen, (80, 160, 60), status['ground']+[(800, 600), (0, 600)])
    if tank2.y < 600:
        tank2.y += 1

    allsprites.update()
    allsprites.draw(screen)
    # here we call the game logic!

    pygame.display.flip()
pygame.quit()
sys.exit()