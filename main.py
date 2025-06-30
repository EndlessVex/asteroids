import pygame
from constants import *
from player import *

def main():
    game_start = 1
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # Game Loop
    while game_start == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        player.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        print(dt)

if __name__ == "__main__":
    main()