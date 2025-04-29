import pygame
import sys

from src.constants import *

from objects.player import Player
from objects.asteroid import Asteroid
from objects.asteroidfield import AsteroidField
from objects.shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # player
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (updatables, drawables, shots)

    player = Player(player_x, player_y)

    asteroid_field = AsteroidField()

    updatables.add(player)
    updatables.add(asteroid_field)
    updatables.add(asteroids)

    drawables.add(player)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill("black")

        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.collides(asteroid):
                    shot.kill()
                    asteroid.split()

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # limit FPS to 60 
        # decouples game speed from speed drawn on screen
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()