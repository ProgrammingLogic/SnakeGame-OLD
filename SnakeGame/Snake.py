import logging


class Snake:
    location = {
        'x': 100,
        'y': 100,
    }
        
    def __init__(self):
        self.logger = logging.getLogger(__name__)
