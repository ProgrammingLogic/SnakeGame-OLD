import pygame
import random
from pygame.locals import *
import os

class SnakeBody(pygame.Rect):
    """
    A body part of the snake.
    """

    def __init__(self, snake, turn_history, direction, x, y, speed, screen, indice, *args, **kargs):
        super(SnakeBody, self).__init__(x, y, 30, 30)
        self.snake = snake
        self.directions = ['north', 'south', 'east', 'west']
        self.direction = direction
        self.speed = speed
        self.screen = screen
        self.screen_size = self.screen.get_size()
        self.turn_history = []
        self.indice = indice
   

    def update(self):
        """
        Updates the SnakeBody.
        """
        self.update_movement()
        self.update_direction()


    def update_direction(self):
        """
        Updates the direction of the SnakeBody.
        """
        if len(self.turn_history) > 0:
            for num, turn in enumerate(self.turn_history):
                if not turn['turned']:
                    if self.indice > 1:
                        print(turn['turned'])
                    if self.snake.size - 1 == self.indice and self.indice > 1:
                        print('left: ' + str(self.left) + ' x: ' + str(turn['x']) + ' top: ' + str(self.top) + ' y: ' + str(turn['y']))

                    if self.left == turn['x'] and self.top == turn['y']:
                        self.change_direction(turn['direction'])
                        self.turn_history[num]['turned'] = True


    def draw(self, background):
        """
        Draws the SnakeBody.
        """
        background.fill((255,255,255), self)


    def update_movement(self):
        """
        Updates the snake movement.
        """
        if self.direction == 'north':
            # If we are on the top part of the screen
            if self.top < 0 + self.speed:
                self.set_pos(self.left, self.screen_size[1])
            else:
                self.move_ip(0, -self.speed)
        elif self.direction == 'south':
            # If we are on the bottom part of the screen
            if self.top > self.screen_size[1] - self.speed:
                self.set_pos(self.left, self.speed)
            else:
                self.move_ip(0, self.speed)
        elif self.direction == 'west':
            # If we are on the left part of the screen
            if self.left < self.speed:
                self.set_pos(self.screen_size[0] - self.speed, self.top)
            else:
                self.move_ip(-self.speed, 0)
        elif self.direction == 'east':
            # If we are on the right side of the screen
            if self.left > self.screen_size[0] - self.speed:
                self.set_pos(self.speed, self.top)
            else:
                self.move_ip(self.speed, 0)


    def set_pos(self, x, y):
        """
        Sets the snakes position.
        """
        self.top = y
        self.left = x

    def change_direction(self, direction):
        """
        Changes the direction of the SnakeBody.
        """
        direction = direction.lower()
        
        if direction in self.directions:
            self.direction = direction
        else:
            raise Exception('Invalid direction.')
    

class Sprite:
    """
    A Sprite for drawing stuff to the screen.
    """
    def __init__(self, game, screen, position = None):
        self.game = game
        self.screen = screen
        self.position = position
        self.screen_size = self.screen.get_size()

class Coin(Sprite):
    """
    A Coin that the snake picks up.
    """
    def __init__(self, *args, **kargs):
        super(Coin, self).__init__(*args, **kargs)
        self.rectangle = pygame.Rect(self.position, (15, 15))


    def draw(self, background):
        background.fill((255,255,255), self.rectangle)

    def update(self):
        pass


class Snake(Sprite):
    """
    The class for the Snake that the player controls.
    """
    def __init__(self, *args, **kargs):
        super(Snake, self).__init__(*args, **kargs)

        self.position = (self.screen_size[0] / 2, self.screen_size[1] / 2)
        self.size = 1
        self.speed = 3
        self.directions = ['north', 'south', 'east', 'west']
        self.direction = 'south'
        self.turns = []
        self.body_parts = [SnakeBody(self, self.turns, self.direction, self.position[0], self.position[1], self.speed, self.screen, 0)]

    def draw(self, background):
        """
        Draws the snake to the screen.
        """
        for part in self.body_parts:
            part.draw(background)

    def update(self):
        """
        Updates the Snake object.
        """
        self.check_collisions()

        for part in self.body_parts:
            part.update()


    def change_direction(self, direction):
        if direction.lower() in self.directions:
            self.direction = direction.lower()

            x = self.body_parts[0].left
            y = self.body_parts[0].top

            turn = {'x': x, 'y': y, 'direction': direction, 'size': self.size, 'turned': False} 

            self.turns.append(turn)

            for num, part in enumerate(self.body_parts):
                if num == 0:
                    part.change_direction(turn['direction'])
                
                elif num == 1 or num is not (len(self.body_parts) - 1):
                    part.turn_history.append(turn)
        else:
            raise Exception('Invalid direction.')
    

    def check_collisions(self):
        """
        Checks whether the snake is colliding with any coins.
        """
        coin = self.game.coins[-1]

        if not coin.rectangle.collidelist(self.body_parts):
            self.score()

    def set_pos(self, x, y):
        """
        Sets the snakes position.
        """
        self.position = (x, y)

    def move(self, num_x, num_y):
        """
        Moves the Snake the specified amount.
        """
        self.position = (self.position[0] + num_x, self.position[1] + num_y)

    def score(self):
        """ 
        Scores a point.
        """
        self.size += 1
        self.add_body_part()
        self.game.add_coin()
        print(self.size)

    def add_body_part(self):
        previous_part = self.body_parts[-1]
        direction = previous_part.direction
        x = 0
        y = 0

        if direction == 'north':
            y = previous_part.top + 30
            x = previous_part.left
        elif direction == 'east':
            y = previous_part.top
            x = previous_part.left - 30
        elif direction == 'west':
            y = previous_part.top
            x = previous_part.left + 30
        elif direction == 'south':
            y = previous_part.top - 30
            x = previous_part.left

        # print(x, y)
        # print(previous_part.left, previous_part.top)
        self.body_parts.append(SnakeBody(self, self.turns, direction , x, y, self.speed, self.screen, len(self.body_parts)))
    

class Game:
    """
    The Main Game class.

    Handles the initialization, game loop, and much more.
    """
    def __init__(self):
        pygame.init()

        self.running = True
        self.screen = pygame.display.set_mode((2000,1000))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        pygame.display.set_caption('Snake Game')
        pygame.mouse.set_visible(0)
        self.clock = pygame.time.Clock()
        self.snake = Snake(self, self.screen)
        self.coins = []
        self.add_coin()

    def game_loop(self, fps):
        """
        The primary game loop for the game.
        """
        self.clock.tick(60)
        self.update_engine()
        self.update_graphics()
        
        return self.running

    def update_engine(self):
        """
        Updates objects in the engine.
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
        
            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    self.snake.change_direction('south')
                elif event.key == K_UP:
                    self.snake.change_direction('north')
                elif event.key == K_RIGHT:
                    self.snake.change_direction('east')
                elif event.key == K_LEFT:
                    self.snake.change_direction('west')
                    
        self.snake.update()

    def update_graphics(self):
        """
        Applies the graphic updates to the screen.
        """
        self.background.fill((0, 0, 0))

        self.snake.draw(self.background)
        self.coins[-1].draw(self.background)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def quit(self):
        """
        Quits the game.
        """
        pass

    def add_coin(self):
        """
        Adds a coin to the game.
        """
        self.coins.append(Coin(self, self.screen, self.find_coin_position()))

    def find_coin_position(self):
        """
        Finds a position for a new coin.
        """
        position = None

        while True:
            position = (random.randrange(0, self.screen.get_size()[0]), random.randrange(0, self.screen.get_size()[1]))
            test_rect = pygame.Rect(position, (15, 15))
            if test_rect.collidelist(self.snake.body_parts):
                break
            else:
                continue

        return position

            
        

def init_game():
    """
    Initializes the Snake Game.
    """
    game = Game()
    running = True

    while running:
        running = game.game_loop(60)

    game.quit()
    


if __name__ == '__main__':
    init_game()
