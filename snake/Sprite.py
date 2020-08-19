import pygame
from pygame.locals import *

class Sprite:
    """
    A entity inside the Game.

    :param sprite_type: 
                        The type of Sprite. Valid options are:
                        'polygon' - pygame.Rect object(s) to be drawn to surfaces.
                        'image' - pygame.Surface object(s) to be drawn to surfaces.
    :param position: A tuple representing the (x, y) position of the Sprite.
    :param images:      Valid inputs are:
                        A list of pygame.Surface objects that will be drawn to a surface.
                        A single pygame.Surface object that will be drawn to a surface.
    :param polygons:    Valid inputs are:
                        A list of pygame.Rect objects that will be drawn to a surface.
                        A single pygame.Rect object that will be drawn to a surface.
    """
    def __init__(self, sprite_type, position = (0, 0), images = None, polygons = None):
        sprite_types = ['polygon', 'image']

        if not sprite_type in sprite_types:
            raise Exception('Invalid Sprite Type.')

        if sprite_type == 'polygon':
            # Create a polygon sprite
            if polygons is None:
                raise Exception('No polygons defined.')

            if type(polygons) is list:
                for polygon in polygons:
                    if not type(polygon) == pygame.Rect:
                        raise Exception(str(polygon) + ' is not a pygame.Rect object.')

                    self.polygons = polygons.copy()

            elif type(polygons) == pygame.Rect:
                self.polygons = [polygon]

            else:
                raise Exception(str(polygon) + ' is not a a pygame.Rect object.')


        elif sprite_type == 'image':
            # Create a image sprite.
            if images is None:
                raise Exception('No images defined.')

            if type(images) is list:
                for image in images:
                    if not type(image) == pygame.Surface:
                        raise Exception(str(polygon) + ' is not a pygame.Surface object.')

                    self.polygons = polygons.copy()

            elif type(images) is pygame.Surface:
                self.images = [images]

            else:
                raise Exception(str(images) + ' is not a a pygame.Surface object.')

        self.position = position
        self.sprite_type = sprite_type
