import pygame
import os

class Game:
    """
    The Main Game class.

    Handles the initialization, game loop, and much more.
    """
    def __init__(self):
        pygame.init()

        screen = pygame.display.setmode((600,600))
        pygame.display.set_caption('Snake Game')
        pygame.mouse.set_visible(0)

    def game_loop(self):
        pass

def init_game(game):
    """
    Initializes the Snake Game.
    """
    game = Game()

if __name__ == '__main__':
    game = None

    init_game(game)

    # The Game Loo
    game.game_loop()
