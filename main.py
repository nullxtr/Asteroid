import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    running = True

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    cl = pygame.time.Clock()
    player = Player(SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2)
    dt = 0


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        dt = cl.tick(60) / 1000

if __name__ == "__main__":
    main()    