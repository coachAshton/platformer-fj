import pygame
import random

class Platform(pygame.Rect):
    def intersectsPlatforms(self, platforms):
        for platform in platforms:
            inflated = platform.inflate(25, 25)
            if self.colliderect(inflated):
                return True
        return False

class Map:
    def __init__(self, width, height):
        self.platforms = []
        for i in range(20):
            rect = Platform(random.randint(0, width), random.randint(0, height), random.randint(60, 180), 40)
            while rect.intersectsPlatforms(self.platforms):
                rect = Platform(random.randint(0, width), random.randint(0, height), random.randint(60, 180), 40)
            self.platforms.append(rect)

        self.platforms.append(Platform(0, height - 290, width, 1000))

    def move(self, dx, dy):
        for platform in self.platforms:
            if platform is not self.platforms[-1]:
                platform.x += dx
                platform.y += dy
                
    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, (180, 90, 240), platform)
