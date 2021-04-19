import random

import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom

from utils import wrap_position

UP = Vector2(0, -1)


class AntRandomWork:
    def __init__(self, position, velocity=Vector2(UP)):
        self.direction = Vector2(UP)
        self.position = Vector2(position)
        self.sprite = pygame.Surface((10, 20))
        self.radius = self.sprite.get_height() / 2
        self.velocity = Vector2(velocity)

        self.sprite.fill((255, 255, 255))

    def move(self, surface):
        angle = random.randint(-5, 5)
        self.direction.rotate_ip(angle)
        self.velocity = self.velocity.rotate(angle)
        self.position = wrap_position(self.position + self.velocity, surface)

    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

    # def collides_with(self, other_obj):
    #     distance = self.position.distance_to(other_obj.position)
    #     return distance < self.radius + other_obj.radius


class AntSimulation:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ant Simulation')
        self.__screen = pygame.display.set_mode((800, 600))
        self.__clock = pygame.time.Clock()

        self.__ant_random_walk = AntRandomWork((400, 300))

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
        self.__ant_random_walk.move(self.__screen)

    def __draw(self):
        self.__screen.fill((0, 0, 0))
        self.__ant_random_walk.draw(self.__screen)

        pygame.display.flip()


if __name__ == '__main__':
    simulation = AntSimulation()
    simulation.main_loop()
