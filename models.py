import random

import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom

from my_logger import logger
from world import SCREEN_WIDTH, SCREEN_HEIGHT

UP = Vector2(0, -1)


class Ant(pygame.sprite.Sprite):
    def __init__(self, position, angle=0, world=None, ):
        super(Ant, self).__init__()

        self.__direction = Vector2(UP)
        self.__position = Vector2(position)
        self.__velocity = Vector2(UP)

        self.__size = Vector2((10, 20))
        self.__sprite = pygame.Surface(self.__size)
        self.__radius = self.__sprite.get_height() / 2

        self.__velocity.rotate_ip(angle)
        self.__direction.rotate_ip(angle)

        self.__sprite.fill((255, 255, 255))
        self.__rect = self.__sprite.get_rect(center=position)

        self.__world = world
        self.__prev_area = None
        self.__cur_area = None
        self.__next_area = None
        self.__target = None

        self.__state = 'toFood'  # toHome

    def update(self):
        if self.__target:
            angle = self.__direction.angle_to(self.__target)
            self.__direction.rotate_ip(angle)
            self.__velocity = self.__velocity.rotate(angle)

        self.__limit_position()

        self.__cur_area = self.__world.get_area(self.__position)
        if self.__prev_area != self.__cur_area:
            self.__world.marker(self.__position, self.__state)
            logger.debug(f"area change; {self.__prev_area} -> {self.__cur_area}")
            self.__world.debug_output()
            self.__prev_area = self.__cur_area

    def find_food(self):
        self.__state = 'toHome'  # toHome

    def target(self, position):
        self.__target = position

    def __limit_position(self):
        self.__position = self.__position + self.__velocity
        if self.__position[0] < 10:
            self.__position[0] = 10
        elif self.__position[0] > SCREEN_WIDTH - 10:
            self.__position[0] = SCREEN_WIDTH - 10
        if self.__position[1] < 10:
            self.__position[1] = 10
        elif self.__position[1] > SCREEN_HEIGHT - 10:
            self.__position[1] = SCREEN_HEIGHT - 10

    def draw(self, surface):
        angle = self.__direction.angle_to(UP)
        rotated_surface = rotozoom(self.__sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.__position - rotated_surface_size / 2
        surface.blit(rotated_surface, blit_position)
        # surface.blit(self.__sprite, self.__rect)

    # def collides_with(self, other_obj):
    #     distance = self.position.distance_to(other_obj.position)
    #     return distance < self.radius + other_obj.radius


# class AntRandomWork:
#     def __init__(self, position, world=None, velocity=Vector2(UP)):
#         self.direction = Vector2(UP)
#         self.position = Vector2(position)
#         self.sprite = pygame.Surface((10, 20))
#         self.radius = self.sprite.get_height() / 2
#         self.velocity = Vector2(velocity)
#
#         self.sprite.fill((255, 255, 255))
#
#         self.__world = world
#         self.__prev_area = None
#         self.__cur_area = None
#         self.__next_area = None
#
#         self.__state = 'toFood'  # toHome
#
#     def move(self):
#         angle = random.randint(-5, 5)
#         self.direction.rotate_ip(angle)
#         self.velocity = self.velocity.rotate(angle)
#
#         # self.position = wrap_position(self.position + self.velocity, surface)
#         self.position = self.position + self.velocity
#         if self.position[0] < 10:
#             self.position[0] = 10
#         elif self.position[0] > SCREEN_WIDTH - 10:
#             self.position[0] = SCREEN_WIDTH - 10
#
#         if self.position[1] < 10:
#             self.position[1] = 10
#         elif self.position[1] > SCREEN_HEIGHT - 10:
#             self.position[1] = SCREEN_HEIGHT - 10
#
#         self.__cur_area = self.__world.get_area(self.position)
#         if self.__prev_area != self.__cur_area:
#             self.__world.marker(self.position, self.__state)
#             logger.debug(f"area change; {self.__prev_area} -> {self.__cur_area}")
#             self.__world.debug_output()
#             self.__prev_area = self.__cur_area
#
#     def draw(self, surface):
#         angle = self.direction.angle_to(UP)
#         rotated_surface = rotozoom(self.sprite, angle, 1.0)
#         rotated_surface_size = Vector2(rotated_surface.get_size())
#         blit_position = self.position - rotated_surface_size / 2
#         surface.blit(rotated_surface, blit_position)
#
#     # def collides_with(self, other_obj):
#     #     distance = self.position.distance_to(other_obj.position)
#     #     return distance < self.radius + other_obj.radius

