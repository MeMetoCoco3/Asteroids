from circleshape import CircleShape
import pygame
import constants


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return (a, b, c)

    def draw(self, screen):
        print("drawing!")
        triangle = self.triangle()
        pygame.draw.polygon(screen, "white", triangle, 2)

    def move(self, dt):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += direction * dt * constants.PLAYER_SPEED

    def rotate(self, dt):
        self.rotation += dt * constants.PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(dt)

        if keys[pygame.K_d]:
            self.rotate(-dt)

        if keys[pygame.K_w]:
            self.move(dt)
