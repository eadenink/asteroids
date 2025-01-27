import sys

import pygame

import groups
from asteroid_field import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    screen_center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    player = Player(*screen_center)
    AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        for obj in groups.updatable:
            obj.update(dt)
        for obj in groups.drawable:
            obj.draw(screen)

        for asteroid in groups.asteroids:
            for shot in groups.shots:
                if shot.is_colliding_with(asteroid):
                    shot.kill()
                    asteroid.kill()

            if asteroid.is_colliding_with(player):
                sys.exit("Game Over!")

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
