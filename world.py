import random

import pygame
from pygame.math import Vector2

from my_logger import logger

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Marker:
    ALPHA_DISCOUNTER = 2

    def __init__(self, position, mode='toFood'):
        self.__alpha = 255
        self.__counter = 0
        self.__size = Vector2((6, 6))

        self.__surf = pygame.Surface(self.__size)
        if mode == 'toFood':
            pygame.draw.circle(self.__surf, BLUE, self.__size / 2, (self.__size / 2)[0])
        else:
            pygame.draw.circle(self.__surf, GREEN, self.__size / 2, (self.__size / 2)[0])
        # self.__surf.fill((255, 255, 255))
        self.__rect = self.__surf.get_rect(center=position)
        self.__surf.set_alpha(self.__alpha)

    def update(self):
        self.__counter += 1
        if self.__counter % Marker.ALPHA_DISCOUNTER == 0:
            self.__counter = 0
            self.__alpha -= 1

    def apply_alpha(self):
        if self.__alpha > 0:
            self.__surf.set_alpha(self.__alpha)
            return True
        return False

    def draw(self, surface):
        surface.blit(self.__surf, self.__rect)


class Area:
    def __init__(self, index=0):
        self.__index = index
        y = (index // World.WORLD_WIDTH) * World.AREA_HEIGHT
        x = (index % World.WORLD_WIDTH) * World.AREA_WIDTH
        self.__position = Vector2((x, y)) + Vector2(World.AREA_SIZE) / 2

        self.__to_food = 0
        self.__to_home = 0

    @property
    def index(self):
        return self.__index

    @property
    def position(self):
        return self.__position

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
    AREA_WIDTH = 40
    AREA_HEIGHT = 40
    AREA_SIZE = (AREA_WIDTH, AREA_HEIGHT)

    WORLD_WIDTH = SCREEN_WIDTH // AREA_WIDTH
    WORLD_HEIGHT = SCREEN_HEIGHT // AREA_HEIGHT

    AROUND_AREAS = (
        Vector2((AREA_WIDTH, 0)),
        Vector2((-AREA_WIDTH, 0)),
        Vector2((0, AREA_HEIGHT)),
        Vector2((0, -AREA_HEIGHT)),

        Vector2((AREA_WIDTH, AREA_HEIGHT)),
        Vector2((AREA_WIDTH, -AREA_HEIGHT)),
        Vector2((-AREA_WIDTH, AREA_HEIGHT)),
        Vector2((-AREA_WIDTH, -AREA_HEIGHT)),
    )

    def __init__(self, marker_callback=None):
        self.__marker_callback = marker_callback
        self.__area_list = list()
        for i in range(World.WORLD_WIDTH * World.WORLD_HEIGHT):
            self.__area_list.append(Area(i))

    def marker(self, position, state='toFood'):
        idx = self.get_area(position)
        self.__area_list[idx].marker(state)
        if self.__marker_callback:
            self.__marker_callback(Marker(position, state))

    def get_next_idx(self, cur, prev=None):
        # todo; 주변 8개의 맵 정보를 읽어서 처리한다.
        areas = list()
        center = self.get_position(cur)
        for vec in World.AROUND_AREAS:
            try:
                pos = center + vec
                index = self.get_area(pos)
                if index == prev:
                    continue
                areas.append(index)
            except Exception as ex:
                logger.debug(f"{ex}")
        random.shuffle(areas)
        return areas[0]

    @staticmethod
    def get_area(position):
        if position[0] < 0 or position[0] > SCREEN_WIDTH - 1 or \
                position[1] < 0 or position[1] > SCREEN_HEIGHT - 1:
            raise Exception(f"out of range; {position}")
        col_ = position[0] // World.AREA_WIDTH
        row_ = position[1] // World.AREA_HEIGHT
        return int(row_ * World.WORLD_WIDTH + col_)

    def get_position(self, index):
        return self.__area_list[index].position

    def debug_output(self):
        # logger.debug(f"AREA to food information")
        msg = ''
        for i, a in enumerate(self.__area_list):
            if a.to_food == 0:
                continue
            # logger.debug(f"to food idx; {i}, value; {a.to_food}")
            msg += f"{i, a.to_food, a.to_home}, "
            if i % 6 == 0:
                msg += '\n'
        logger.debug(f"AREA to food information. \n{msg}")


if __name__ == '__main__':
    w = World()
    pos_ = Vector2((210, 150))
    index_ = w.get_area(pos_)
    center_ = w.get_position(index_)
    logger.debug(f"{center_}")

    for v_ in World.AROUND_AREAS:
        pos1 = center_ + v_
        logger.debug(f"{pos1}, {w.get_area(pos1)}")

    # # c_pos = w.get_position(index_)
    # logger.debug(f"org pos; {pos_}, idx; {index_}, pos; {c_pos}")
