import pygame

class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.vy = 0
        self.original_image = pygame.image.load("tank.png").convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.aim_angle = 270
        self.rect = self.image.get_rect(center=(x, y))

        # Rotation angle
        self.angle = 0

    def update(self):
        center = self.rect.center
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=center, topleft=(self.x, self.y))