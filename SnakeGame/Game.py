import logging
from .Snake import Snake


class Game:
    logger = None
    running = True
    iterations = 0
    max_iterations = 10
    snake = None


    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    
        self.snake = Snake()


    def loop(self):
        while self.running:
            self.logger.debug(f"""Starting iteration {self.iterations}""")

            self.snake.location['x'] += 5
            self.snake.location['y'] += 5
            
            self.logger.info(f"""Snake Location: [{self.snake.location["x"]}, {self.snake.location["y"]}]""")
            self.iterations += 1


            # Determine if we should stop the game
            if (self.iterations > self.max_iterations):
                self.running = False
