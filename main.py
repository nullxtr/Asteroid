import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    cl = pygame.time.Clock()
    player = Player(SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2)
    dt = 0


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.isColliding(asteroid):
                    bullet.kill()
                    asteroid.split()

            if asteroid.isColliding(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        
        dt = cl.tick(60) / 1000

if __name__ == "__main__":
    main()