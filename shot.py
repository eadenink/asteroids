import pygame

import groups
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    containers = (groups.shots, groups.updatable, groups.drawable)

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.velocity * dt
