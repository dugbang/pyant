import random

import pygame
from pygame.math import Vector2

from models import Ant
from my_logger import logger
from world import SCREEN_SIZE, World


class AntSimulation:
    DEBUG_OUTPUT = pygame.USEREVENT + 1

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ant Simulation')
        pygame.time.set_timer(AntSimulation.DEBUG_OUTPUT, 30 * 1000)

        self.__screen = pygame.display.set_mode(SCREEN_SIZE)
        self.__clock = pygame.time.Clock()

        self.__ant_sprites = list()
        self.__marker_sprites = list()

        self.__world = World(marker_callback=self.__marker_sprites.append)

    def main_loop(self):

        for i in range(15):
            self.__ant_sprites.append(Ant(Vector2((250, 350)), angle=random.randint(0, 360), world=self.__world))

        while True:
            self.__handle_input()
            self.__process_game_logic()
            self.__draw()
            self.__clock.tick(30)

    def __handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

            elif event.type == AntSimulation.DEBUG_OUTPUT:
                self.__world.debug_output()

        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_t]:
            for ant in self.__ant_sprites:
                self.__test_random_target(ant)

    @staticmethod
    def __test_random_target(ant):
        target = Vector2((random.randint(20, 780), random.randint(20, 580)))
        logger.debug(f"new target...; {target}")
        ant.target(target)

    def __process_game_logic(self):
        for ant in self.__ant_sprites:
            ant.update()
            if ant.arrive_target() is True:
                self.__world.marker(ant.position, state='toHome')
                self.__test_random_target(ant)

        for marker in self.__marker_sprites:
            marker.update()
            if marker.apply_alpha() is False:
                self.__marker_sprites.remove(marker)

    def __draw(self):
        self.__screen.fill((0, 0, 0))
        for marker in self.__marker_sprites:
            marker.draw(self.__screen)
        for ant in self.__ant_sprites:
            ant.draw(self.__screen)

        pygame.display.flip()


if __name__ == '__main__':
    simulation = AntSimulation()
    simulation.main_loop()
