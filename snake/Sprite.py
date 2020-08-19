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
            self.polygons = []

            if polygons is None:
                raise Exception('No polygons defined.')

            if type(polygons[0]) is list:
                self.add_polygons(*polygons)
            else:
                self.add_polygons(polygons)


        elif sprite_type == 'image':
            # Create a image sprite.
            self.images = []

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
        self.update_pos_vars()
        self.sprite_type = sprite_type


    def update(self):
        """
        Updates the Sprite instance.
        """
        self.update_events(pygame.event.get())
        self.update_sprite()


    def update_events(self, *events):
        """
        Updates the Sprite based on Events occuring in the Game.

        :param *events: A list of events that occured during the call.
        """
        pass


    def update_sprite(self):
        """
        Updates internal parts of the Sprite.
        """
        pass


    def update_pos_vars(self):
        """
        Updates the position variables of the Sprite.
        """
        self.x = self.position[0]
        self.y = self.position[1]


    def draw(self, surface):
        """
        Draws the Sprite to the given surface.

        :param surface: A pygame.Surface object the Sprite will be drawn onto.
        """
        if self.sprite_type == 'polygon':
            self.draw_polygons(surface)
        elif self.sprite_type == 'image':
            self.draw_images(surface)


    def add_polygons(self, *polygons):
        """
        Adds a selection of polygons to the Sprite.

        :param *polygons: Valid Inputs:
                          A single list containing the polygon and color: [shape, color] 
                          A list of lists containing different polygons and their color: [[shape, color], ..]
        """

        for polygon in polygons:
            if not type(polygon[0]) == pygame.Rect:
                raise Exception(str(polygon[0]) + ' is not a pygame.Rect object.')
            if not type(polygon[1]) == pygame.Color:
                raise Exception(str(polygon[1]) + ' is not a pygame.Color object.')

            self.polygons.append(polygon.copy())


    def draw_polygons(self, surface):
        """
        Draws the polygons contained in the Sprite to the given surface.

        :param surface: The pygame.Surface object that the polygons will be drawn onto.
        """
        width = surface.get_width()
        height = surface.get_height()
        collision_rect = pygame.Rect(0, 0, width, height)

        for polygon_parts in self.polygons:

            shape = polygon_parts[0]
            color = polygon_parts[1]

            new_pos = (self.x + shape.x, self.y + shape.y)
            polygon = shape.move(new_pos)
            
            # If the Rectangle is inside the surface.
            if not collision_rect.colliderect(polygon):
                print('not drawing!!!')
                continue

            surface.fill(color, polygon)


    def draw_images(self, surface):
        """
        Draws the images contained in the Sprite to the given surface.

        :param surface: The pygame.Surface object that the polygons will be drawn onto.
        """
        pass


def test_sprite():
    """
    Tests the Sprite class to confirm it works as intended.
    """
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
    test_sprite()
