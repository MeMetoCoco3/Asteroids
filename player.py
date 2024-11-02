from circleshape import CircleShape
from shoot import Shoot
from constants import *
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return (a, b, c)

    def shoot(self):
        if self.timer <= 0:
            s = Shoot(self.position[0], self.position[1], SHOOT_RADIUS)
            s.velocity = pygame.Vector2(0, 1)
            # Cuidadito con rotate, que no cambia, solo devuelve el vector rotado.
            s.velocity = s.velocity.rotate(self.rotation)
            self.timer = PLAYER_SHOOT_COUNTDOWN
        return

    def draw(self, screen):
        triangle = self.triangle()
        pygame.draw.polygon(screen, "white", triangle, 2)

    def move(self, dt):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * dt * PLAYER_SPEED

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt)

        if keys[pygame.K_d]:
            self.rotate(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()
            print("Shooting!")

        if keys[pygame.K_w]:
            self.move(dt)

        self.timer -= dt
