import pygame
from player import Player


class Scene:
    def __init__(self, sw, sh, gravity):
        self.gravity = 10

        self.bottom = sh
        self.player1 = Player(pygame.Rect(0, 0, 20, 20), (200, 23, 188), self)

    def update(self):
        self.player1.update()

    def draw(self, screen):
        self.player1.draw(screen)