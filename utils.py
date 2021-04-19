import random

from pygame.math import Vector2

from my_logger import logger


def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h)


UP = Vector2(0, -1)


if __name__ == '__main__':
    direction = Vector2((0, -1))
    logger.debug(f"{direction}")
    logger.debug(f"{direction.rotate_ip(30)}")
    logger.debug(f"{direction.angle_to(UP)}")

    velocity = Vector2((0, -1))
    logger.debug(f"{velocity}")
    logger.debug(f"{velocity.rotate(30)}")
    velocity = velocity.rotate(30)
    logger.debug(f"{velocity.rotate(30)}")
