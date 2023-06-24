import pygame
from player import Player
from map import Map

class Scene:
    def __init__(self, sw, sh, gravity):
        self.gravity = 2

        self.bottom = sh
        self.map = Map(2000, 1000)
        self.player1 = Player(pygame.Rect(0, 0, 20, 20), (200, 23, 188), self)

    def update(self):
        dx, dy = self.player1.update()
        self.map.move(dx, dy)

    def draw(self, screen):
        self.map.draw(screen)
        self.player1.draw(screen)