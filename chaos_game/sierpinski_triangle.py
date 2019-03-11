from pygame.locals import *
from pygame import Vector2, Surface
import pygame

import random
from sys import argv


def convert2int(t):
    return list(map(int, t))


def new_point_triangle():
    attractor_point = random.choice(vertices)
    path = attractor_point - points[-1]
    _ = points[-1] + path.normalize() * path.length() / 2
    points.append(_)
    return _


def generate_surface(iterations):
    surf = Surface((WIDTH, HEIGHT))

    for _ in range(iterations):
        new_point = new_point_triangle()
        surf.set_at(convert2int(new_point), WHITE)

    return surf


pygame.init()

WIDTH, HEIGHT = SIZE = 1000, 1000

screen = pygame.display.set_mode(SIZE)

BLACK = Color('black')
WHITE = Color('white')
GREEN = Color('green')

font = pygame.font.SysFont('courier', 30)

vertices = [
    Vector2(200, 200),
    Vector2(505, 505),
    Vector2(30, 400)
]


points = [Vector2(201, 200)]

iterations = 0
static = False
surface = None

try:
    iterations = int(argv[1])
    static = True
    surface = generate_surface(iterations)

except (ValueError, IndexError):
    pass


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if static:
        screen.fill(BLACK)

        screen.blit(surface, (0, 0))

        for point in vertices:
            pygame.draw.circle(screen, GREEN, convert2int(point), 3)

    else:
        for point in points:
            screen.set_at(convert2int(point), WHITE)

        for point in vertices:
            pygame.draw.circle(screen, GREEN, convert2int(point), 3)

        new_point_triangle()

        iterations += 1

    text = font.render('interation: {}'.format(iterations), 4, WHITE)
    screen.fill(BLACK, text.get_rect(x=10, y=10))
    screen.blit(text, text.get_rect(x=10, y=10))

    pygame.display.flip()
