import pygame


class AntSimulation:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ant Simulation')
        self.__screen = pygame.display.set_mode((800, 600))
        self.__clock = pygame.time.Clock()

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
        pass

    def __draw(self):
        self.__screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    simulation = AntSimulation()
    simulation.main_loop()
