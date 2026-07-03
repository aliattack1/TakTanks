import pygame

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("tank.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect = self.image.get_rect(topleft=(self.x, self.y))