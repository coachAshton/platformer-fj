import pygame, sys
from scene import Scene

pygame.init()

SW = 900
SH = 500

SCREEN = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Platformer")

clock = pygame.time.Clock()
FPS = 60

scene = Scene(SW, SH, 10)
run = True

while run:
    clock.tick(FPS)

    scene.update
    scene.draw(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
    pygame.display.update()
