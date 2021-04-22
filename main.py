import pygame
from pygame.math import Vector2

from models import Ant
from world import SCREEN_SIZE, World


class AntSimulation:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ant Simulation')
        self.__screen = pygame.display.set_mode(SCREEN_SIZE)
        self.__clock = pygame.time.Clock()

        self.__ant_sprites = pygame.sprite.Group()
        self.__marker_sprites = pygame.sprite.Group()

        self.__world = World(marker_callback=self.__marker_sprites.add)
        self.__ant = Ant(Vector2(250, 250), angle=30, world=self.__world)

        self.__ant_sprites.add(self.__ant)
        self.__ant.target(Vector2(650, 550))

    def main_loop(self):
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

    def __process_game_logic(self):
        self.__ant_sprites.update()
        self.__marker_sprites.update()

    def __draw(self):
        self.__screen.fill((0, 0, 0))
        for entity in self.__marker_sprites:
            entity.draw(self.__screen)
        for entity in self.__ant_sprites:
            entity.draw(self.__screen)

        pygame.display.flip()


if __name__ == '__main__':
    simulation = AntSimulation()
    simulation.main_loop()
