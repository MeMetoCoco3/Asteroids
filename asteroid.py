from circleshape import CircleShape
from constants import *
import random
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * ASTEROID_SPEED * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        # Was small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        new_angle = random.uniform(20, 50)

        dir_a = self.velocity.rotate(new_angle)
        dir_b = self.velocity.rotate(-new_angle)

        asteroid_a = Asteroid(
            self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS
        )
        asteroid_a.velocity = dir_a * 1.2
        asteroid_b = Asteroid(
            self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS
        )
        asteroid_b.velocity = dir_b * 1.2

        self.kill()
