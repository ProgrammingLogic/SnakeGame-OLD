import logging
import argparse


class Snake:
    location = {
        'x': 100,
        'y': 100,
    }
        
    def __init__(self):
        pass




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

    # Set the log level.
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


def game_loop(running, iterations, max_iterations, snake):
    logger = logging.getLogger(__name__)
    
    while running:
        logger.debug(f"""Starting iteration {iterations}""")

        snake.location['x'] += 5
        snake.location['y'] += 5
        
        logger.info(f"""Snake Location: [{snake.location["x"]}, {snake.location["y"]}]""")
        iterations += 1
        # Determine if we should stop the game
        if (iterations > max_iterations):
            running = False


def main():
    # Logic to start the game
    args = parse_arguments()
    logger = setup_logger(args)

    running = True
    iterations = 0
    max_iterations = 10
    logger.info("Starting game")
    snake = Snake()


    game_loop(running, iterations, max_iterations, Snake)


    # Logic to end the game 
    logger.info("Ending game")


if __name__ == '__main__':
    main()
