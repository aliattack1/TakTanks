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
tank1.aim_angle += 60
tank2 = tank.Tank(640, 400)
tank2.aim_angle -= 60

turn = True

allsprites = pygame.sprite.Group()
allsprites.add(tank1)
allsprites.add(tank2)
tanks = [tank1, tank2]

def angl():
    tank1.aim_angle -= 1
    return True

anglon = False

def angr():
    tank1.aim_angle += 1
    return True

bullet = {'current':False, 'x':0, 'y':0, 'vx':0, 'vy':0, 'damage':0}

def shot(tank: tank.Tank):
    global bullet
    x, y = tank.rect.center
    bullet['current'] = True
    bullet['x'] = x
    bullet['y'] = y
    bullet['vx'] = tank.power * math.cos(math.radians(tank.aim_angle))
    bullet['vy'] = tank.power * math.sin(math.radians(tank.aim_angle))


angron = False

while running:
    mouse = pygame.mouse.get_pos()
    clock.tick(FPS)
    if anglon:
        angl()
    if angron:
        angr()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[1] > 625 and mouse[1] < 675:
                    if 50 < mouse[0] and mouse[0] < 150:
                        shot(tank1)
                    elif 245 < mouse[0] and mouse[0] < 345:
                        anglon = angl()
                    elif 355 < mouse[0] and mouse[0] < 455:
                        angron = angr()
                    elif 545 < mouse[0] and mouse[0] < 645:
                        print('powerdown')
                    elif 655 < mouse[0] and mouse[0] < 755:
                        print('powerup')
            if event.type == pygame.MOUSEBUTTONUP:
                anglon, angron = False, False

    keys = pygame.key.get_pressed()
    screen.fill((255,255,255))
    # here i will add all the drawings like the tanks and the ground later

    # ground
    pygame.draw.polygon(screen, (80, 160, 60), status['ground']+[(800, 600), (0, 600)])


    # tanks logic
    for ind, tank in enumerate(tanks):
        # angle logic
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
        angle = math.radians(tank.aim_angle)

        if ind == 0 and turn:
            pygame.draw.line(screen, (200, 200, 200), tank.rect.center,(tank.rect.center[0] + 600 * math.cos(angle), tank.rect.center[1] + 600 * math.sin(angle)), 2)


        pygame.draw.line(screen, (20, 70, 120), tank.rect.center,(tank.rect.center[0] + 40 * math.cos(angle), tank.rect.center[1] + 40 * math.sin(angle)), 6)

    # UI panel
    UI_HEIGHT = 100
    pygame.draw.rect(screen, (0, 0, 0), (0, HEIGHT - UI_HEIGHT, WIDTH, UI_HEIGHT))
    pygame.draw.line(screen, (230, 230, 230), (0, HEIGHT - UI_HEIGHT), (WIDTH, HEIGHT - UI_HEIGHT), 2)

    pygame.draw.rect(screen, (200, 50, 50), (50, 625, 100, 50))
    pygame.draw.rect(screen, (100, 100, 100), (245, 625, 100, 50))
    pygame.draw.rect(screen, (100, 100, 100), (355, 625, 100, 50))
    pygame.draw.rect(screen, (160, 160, 160), (545, 625, 100, 50))
    pygame.draw.rect(screen, (160, 160, 160), (655, 625, 100, 50))

    bullet['x'] = bullet['x'] + bullet['vx']
    bullet['y'] = bullet['y'] + bullet['vy']
    bullet['vx'] -= 0.1
    bullet['vy'] += 0.1
    pygame.draw.circle(screen, (250, 0, 0), (bullet['x'], bullet['y'] ), 2, 2)




    allsprites.update()
    allsprites.draw(screen)
    # here we call the game logic!





    pygame.display.flip()
pygame.quit()
sys.exit()