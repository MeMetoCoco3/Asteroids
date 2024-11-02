import pygame
from sys import exit
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shoot


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    g_draw = pygame.sprite.Group()
    g_update = pygame.sprite.Group()
    g_asteroids = pygame.sprite.Group()
    # g_asteroid_field = pygame.sprite.Group()
    g_shoot = pygame.sprite.Group()

    Player.containers = (g_draw, g_update)
    Asteroid.containers = (g_asteroids, g_draw, g_update)
    AsteroidField.containers = g_update
    Shoot.containers = (g_shoot, g_update, g_draw)

    pl = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    as_field = AsteroidField()
    while True:
        screen.fill("black")

        # Listen events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Collision
        for asteroid in g_asteroids:
            if asteroid.check_collision(pl):
                exit(1)
            for bullet in g_shoot:
                if asteroid.check_collision(bullet):
                    # Kill is a built in feature in Pygame
                    asteroid.split()
                    bullet.kill()

        # Update
        for thing in g_update:
            thing.update(dt)

        # Draw
        for thing in g_draw:
            thing.draw(screen)

        # Tick cuts top fps to 60 and returns delta in ms
        dt = clock.tick(60) / 1000

        # print("Starting asteroids!")
        # print(f"Screen width: {constants.SCREEN_WIDTH}")
        # print(f"Screen height: {constants.SCREEN_HEIGHT}")
        pygame.display.flip()


if __name__ == "__main__":
    main()
