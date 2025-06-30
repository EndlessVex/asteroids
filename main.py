import pygame
from constants import *

def main():
    game_start = 1
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Game Loop
    while game_start == 1:
        pygame.Surface.fill(screen, color="black")
        pygame.display.flip()

if __name__ == "__main__":
    main()