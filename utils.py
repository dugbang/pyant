import random

from pygame import Color
from pygame.math import Vector2

from my_logger import logger


def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)


def print_text(surface, text, font, color=Color("tomato")):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center_ = Vector2(surface.get_size()) / 2

    surface.blit(text_surface, rect)


if __name__ == '__main__':
    direction = Vector2((0, -1))
    target = Vector2((1, -1))
    logger.debug(f"{direction.angle_to(target):.3f}")
    # logger.debug(f"{direction}, {direction/2}, {(direction/2)[0]}")
    # logger.debug(f"{direction.rotate_ip(30)}")
    # logger.debug(f"{direction.angle_to(UP)}")
    # pygame.math.Vector2(x1, y1).angle_to((x2, y2))
    # velocity = Vector2((0, -1))
    # logger.debug(f"{velocity}")
    # logger.debug(f"{velocity.rotate(30)}")
    # velocity = velocity.rotate(30)
    # logger.debug(f"{velocity.rotate(30)}")
