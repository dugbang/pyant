import pygame
from pygame.math import Vector2

from models import SCREEN_SIZE, AntRandomWork, World


class AntSimulation:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ant Simulation')
        self.__screen = pygame.display.set_mode(SCREEN_SIZE)
        self.__clock = pygame.time.Clock()

        self.__world = World()
        self.__ant = AntRandomWork(Vector2(SCREEN_SIZE) / 2, world=self.__world)

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
        self.__ant.move(self.__screen)

    def __draw(self):
        self.__screen.fill((0, 0, 0))
        self.__ant.draw(self.__screen)

        pygame.display.flip()


if __name__ == '__main__':
    simulation = AntSimulation()
    simulation.main_loop()
