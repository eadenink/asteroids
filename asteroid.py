import random

import pygame

import groups
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_SPEED_ACCELERATION


class Asteroid(CircleShape):
    containers = (groups.asteroids, groups.updatable, groups.drawable)

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rotation = random.uniform(20, 50)
        split_radius = self.radius - ASTEROID_MIN_RADIUS

        first_split = Asteroid(self.position.x, self.position.y, split_radius)
        second_split = Asteroid(self.position.x, self.position.y, split_radius)

        first_split.velocity = (
            self.velocity.rotate(rotation) * ASTEROID_SPLIT_SPEED_ACCELERATION
        )
        second_split.velocity = (
            self.velocity.rotate(-rotation) * ASTEROID_SPLIT_SPEED_ACCELERATION
        )
