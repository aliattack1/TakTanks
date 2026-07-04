import math

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
tanks = [tank1, tank2]
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


    # tanks logic
    for tank in tanks:
        # angle logic
        tank.x +=1
        x = tank.x + 20
        dx = x % 80
        lx = x - dx

        ind1 = int(lx / 80)
        ind2 = ind1 + 1
        y1 = status['ground'][ind1][1]
        y2 = status['ground'][ind2][1]
        angle_rad = math.atan2(y2-y1, 80)
        angle_deg = math.degrees(angle_rad)
        tank.angle -= (tank.angle - angle_deg) / (1 + math.log(x))

        # gravity logic
        ground_height = y1 + (((y2 - y1) / 80) * dx)
        tank.vy += 0.2
        tank.y += tank.vy

        if tank.y + 22 > ground_height:
            tank.y = ground_height - 22
            tank.vy = 0






    allsprites.update()
    allsprites.draw(screen)
    # here we call the game logic!





    pygame.display.flip()
pygame.quit()
sys.exit()