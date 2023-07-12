import pygame


class Player:
    def __init__(self, rectangle, color, scene):
        self.scene = scene
        self.rectangle = rectangle
        self.color = color
        self.yVel = 0
        self.jumpTimer = 0
        self.jumps = 0

    def update(self, platforms):
        kb = pygame.key.get_pressed()

        return self.move(kb, platforms)

    def move(self, kb, platforms):
        dx = dy = 0
        if kb[pygame.K_SPACE] and self.jumpTimer == 0 and self.jumps < 2:
            dy = -25
            self.jumpTimer = 10
            self.jumps += 1
            self.yVel = 0
        if self.jumpTimer > 0:
            self.jumpTimer -= 1

        if kb[pygame.K_a]:
            dx = -5

        if kb[pygame.K_d]:
            dx = 5

        onPlatform = False
        for platform in platforms:
            if platform.colliderect(self.rectangle):
               # if self.rectangle.bottom <= platform.y:
                self.rectangle.bottom += platform.y - self.rectangle.bottom + 1
                self.jumps = 0
                self.jumpTimer = 0
                onPlatform = True
        if not onPlatform:
            self.yVel += self.scene.gravity
            print("go")


        self.yVel += dy
        yVelCopy = self.yVel

        if self.rectangle.x + dx < self.scene.right / 2 and self.rectangle.x + dx > 0:
            self.rectangle.x += dx
            dx = 0

        if self.rectangle.y + self.yVel > self.scene.bottom / 2:
            self.rectangle.y += self.yVel
            yVelCopy = 0

        if self.rectangle.x + dx < self.scene.right / 2 and self.rectangle.x + dx > 0:
            self.rectangle.x += dx
            dx = 0

        return (-dx, -yVelCopy)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rectangle)