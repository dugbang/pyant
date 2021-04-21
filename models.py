import random

import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom

from my_logger import logger
from utils import wrap_position

UP = Vector2(0, -1)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Marker(pygame.sprite.Sprite):
    ALPHA_DISCOUNTER = 1

    def __init__(self, position):
        self.__alpha = 255
        self.__counter = 0
        self.__size = Vector2((60, 60))

        super(Marker, self).__init__()
        self.__surf = pygame.Surface(self.__size)
        pygame.draw.circle(self.__surf, GREEN, self.__size / 2, (self.__size / 2)[0])
        # self.__surf.fill((255, 255, 255))
        self.__rect = self.__surf.get_rect(center=position)
        self.__surf.set_alpha(self.__alpha)

    def update(self):
        self.__counter += 1
        if self.__counter % Marker.ALPHA_DISCOUNTER == 0:
            self.__counter = 0
            self.__alpha -= 1

        if self.__alpha < 0:
            self.kill()
        else:
            self.__surf.set_alpha(self.__alpha)

    def draw(self, surface):
        surface.blit(self.__surf, self.__rect)


class Area:
    def __init__(self, idx=0):
        y = (idx // World.WORLD_WIDTH) * World.AREA_HEIGHT
        x = (idx % World.WORLD_WIDTH) * World.AREA_WIDTH
        self.__position = Vector2((x, y)) + Vector2(World.AREA_SIZE) / 2

        self.__to_food = 0
        self.__to_home = 0

    @property
    def to_food(self):
        return self.__to_food

    @property
    def to_home(self):
        return self.__to_home

    def marker(self, state):
        if state == 'toFood':
            self.__to_food += 1
        elif state == 'toHome':
            self.__to_home += 1
        else:
            raise Exception(f"Error Ant State; {state}")

    def debug_output(self):
        logger.debug(self.__position)


class World:
    AREA_WIDTH = 100  # 40, 40
    AREA_HEIGHT = 100
    AREA_SIZE = (AREA_WIDTH, AREA_HEIGHT)

    WORLD_WIDTH = SCREEN_WIDTH // AREA_WIDTH
    WORLD_HEIGHT = SCREEN_HEIGHT // AREA_HEIGHT

    def __init__(self):
        self.__area_list = list()
        for i in range(World.WORLD_WIDTH * World.WORLD_HEIGHT):
            self.__area_list.append(Area(i))

    def marker(self, position, state):
        idx = self.get_area(position)
        self.__area_list[idx].marker(state)

    @staticmethod
    def get_area(position):
        col_ = position[0] // World.AREA_WIDTH
        row_ = position[1] // World.AREA_HEIGHT
        return int(row_ * World.WORLD_WIDTH + col_)

    def debug_output(self):
        for i, a in enumerate(self.__area_list):
            if a.to_food == 0:
                continue
            logger.debug(f"to food idx; {i}, value; {a.to_food}")


class AntRandomWork:
    def __init__(self, position, world=None, velocity=Vector2(UP)):
        self.direction = Vector2(UP)
        self.position = Vector2(position)
        self.sprite = pygame.Surface((10, 20))
        self.radius = self.sprite.get_height() / 2
        self.velocity = Vector2(velocity)

        self.sprite.fill((255, 255, 255))

        self.__world = world
        self.__prev_area = None
        self.__cur_area = None
        self.__next_area = None

        self.__state = 'toFood'  # toHome

    def move(self):
        angle = random.randint(-5, 5)
        self.direction.rotate_ip(angle)
        self.velocity = self.velocity.rotate(angle)

        # self.position = wrap_position(self.position + self.velocity, surface)
        self.position = self.position + self.velocity
        if self.position[0] < 10:
            self.position[0] = 10
        elif self.position[0] > SCREEN_WIDTH - 10:
            self.position[0] = SCREEN_WIDTH - 10

        if self.position[1] < 10:
            self.position[1] = 10
        elif self.position[1] > SCREEN_HEIGHT - 10:
            self.position[1] = SCREEN_HEIGHT - 10

        self.__cur_area = self.__world.get_area(self.position)
        if self.__prev_area != self.__cur_area:
            self.__world.marker(self.position, self.__state)
            logger.debug(f"area change; {self.__prev_area} -> {self.__cur_area}")
            self.__world.debug_output()
            self.__prev_area = self.__cur_area

    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size / 2
        surface.blit(rotated_surface, blit_position)

    # def collides_with(self, other_obj):
    #     distance = self.position.distance_to(other_obj.position)
    #     return distance < self.radius + other_obj.radius


if __name__ == '__main__':
    w = World()
    logger.debug(f"{w.get_area(Vector2((10, 50)))}")
