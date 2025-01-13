import pygame

import groups
from circleshape import CircleShape


class Asteroid(CircleShape):
    containers = (groups.asteroids, groups.updatable, groups.drawable)

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.velocity * dt
