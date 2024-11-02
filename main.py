import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    g_draw = pygame.sprite.Group()
    g_update = pygame.sprite.Group()

    Player.containers = (g_draw, g_update)
    pl = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        screen.fill("black")

        # Listen events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

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
