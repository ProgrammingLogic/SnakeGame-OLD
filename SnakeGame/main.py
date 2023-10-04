import logging
import argparse
from .Snake import Snake


class Game:
    running = True
    iterations = 0
    max_iterations = 10
    snake = None


    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)
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


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Play a game called Snake."
    )

    
    # Log level
    parser.add_argument(
        "-v", "--log_level", 
        required=False,
        action="store",
        help="The level of output the application provides.",
        choices=[
            "debug",
            "info",
            "warning",
            "error",
            "critical",
        ],
        default="debug",
    )
    
    return parser.parse_args()


def setup_logger(args):
    # If a log level isn't defined, we just want to use info.
    log_level = logging.INFO

    match args.log_level:
        case "debug":
            log_level = logging.DEBUG
        case "info":
            log_level = logging.INFO
        case "warning":
            log_level = logging.WARNING
        case "error":
            log_level = logging.ERROR
        case "critical":
            log_level = logging.CRITICAL


    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    log_file = "./snake.log"

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.debug("Logger has been initialized")
    return logger




def main():
    # Logic to start the game
    args = parse_arguments()
    logger = setup_logger(args)
    logger.info("Starting game")


    game = Game()
    game.loop()


    # Logic to end the game 
    logger.info("Ending game")


if __name__ == '__main__':
    main()
