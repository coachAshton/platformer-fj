import pygame


class Player:
    def __init__(self, rectangle, color, scene):
        self.scene = scene
        self.rectangle = rectangle
        self.color = color
        self.yVel = 0

    def update(self):
        kb = pygame.key.get_pressed()

        self.move(kb)

    def move(self, kb):
        dx = dy = 0
        if kb[pygame.K_SPACE]:
            dy = -5

        if kb[pygame.K_a]:
            dx = -5

        if kb[pygame.K_d]:
            dx = 5

        if self.rectangle.bottom >= self.scene.bottom:
            self.yVel = 0
        else:
            self.yVel += self.scene.gravity

        self.yVel += dy
        self.rectangle.x += dx
        self.rectangle.y += self.yVel

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle)