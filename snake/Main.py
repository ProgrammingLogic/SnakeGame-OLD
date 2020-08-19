import game
from game.graphics import Sprite, Scene

import pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    surface = pygame.Surface(screen.get_size())
    pygame.display.set_caption('Testing')
    clock = pygame.time.Clock()
    running = True
    
    test_rects = [[pygame.Rect(20, 20, 30, 30), pygame.Color(255,255,255)], [pygame.Rect(120, 20, 30, 30), pygame.Color(255, 255, 255)]]
    sprite = Sprite('polygon', (0, 0), polygons = test_rects)

    while running:
        clock.tick(60)
        sprite.position = (sprite.x + 3, sprite.y + 3)
        sprite.update()
        sprite.update_pos_vars()
        surface.fill((0, 0, 0))
        sprite.draw(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

if __name__ == '__main__':
    main()
