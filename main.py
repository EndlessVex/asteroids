import pygame
from constants import *
from player import *

def main():
    game_start = 1
    dt = 0
    pygame.init()

    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    # Game Loop
    while game_start == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        updatable_group.update(dt)
        for object in drawable_group:
            object.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        #print(dt)

if __name__ == "__main__":
    main()