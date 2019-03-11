from math import sin, cos, pi

from pygame.math import Vector2
import pygame
from pygame.locals import *

pygame.init()


def convert2int(t):
    return list(map(int, t))


def up(start_color: list, index: int):
    for component in range(256):
        new_color = start_color.copy()
        new_color[index] = component
        yield new_color


def down(start_color: list, index: int):
    for component in range(255, -1, -1):
        new_color = start_color.copy()
        new_color[index] = component
        yield new_color


def color_iterator():
    while True:
        yield from up([255, 0, 0], 1)
        yield from down([255, 255, 0], 0)
        yield from up([0, 255, 0], 2)
        yield from down([0, 255, 255], 1)
        yield from up([0, 0, 255], 0)
        yield from down([255, 0, 255], 2)


count = 200
multiple = 1
radius = 400
step = 0.01
center = Vector2(radius, radius)

theta = 2 * pi / count

alpha = lambda n: (theta * n) % count

f_x = lambda n: cos(alpha(n)) * radius + center.x
f_y = lambda n: sin(alpha(n)) * radius + center.y

f = lambda n: Vector2(f_x(n), f_y(n))


BLACK = Color('black')
WHITE = Color('white')
RED = Color('red')

WIDTH, HEIGHT = SIZE = radius * 2, radius * 2
screen = pygame.display.set_mode(SIZE)

color = color_iterator()

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    screen.fill(BLACK)

    c = next(color)

    pygame.draw.circle(screen, c, convert2int(center), radius, 3)

    for n in range(count):
        p1 = f(n)
        p2 = f(multiple * n)
        pygame.draw.line(screen, c, convert2int(p1), convert2int(p2), 1)

    multiple += step

    pygame.display.flip()
