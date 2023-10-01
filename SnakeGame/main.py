import logging
import argparse


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
        default="info",
    )
    
    return parser.parse_args()


def setup_logger():
    base_log_level = logging.DEBUG
    logger = logging.getLogger(__name__)
    logger.setLevel(base_log_level)
    log_file = "./snake.log"

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_log_level = base_log_level
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(file_log_level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_log_level = base_log_level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.debug("Logger has been initialized")


def main():
    # Logic to start the game
    args = parse_arguments()
    setup_logger()
    logger = logging.getLogger(__name__)

    running = True
    iterations = 0
    max_iterations = 10
    logger.info("Starting game")


    while running:
        logger.debug(f"""Iteration {iterations}""")
        iterations += 1
        
        # Determine if we should stop the game
        if (iterations > max_iterations):
            running = False


    # Logic to end the game 
    logger.info("Ending game")


if __name__ == '__main__':
    main()
