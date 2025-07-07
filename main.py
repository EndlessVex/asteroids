import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from bullet import *
from audio import *

### TODO ###
# Add weapon spawns with effects when grabbed along with audio
# Make asteroids more lumpy and varried
# Make hitbox actually correct (a triangle)
# Add Powerups (speed, shield, clear screen)


def main():
    game_start = 1
    dt = 0
    pygame.init()

    game_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    font = pygame.font.Font('freesansbold.ttf', 32)

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    powerup_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    Shot.containers = (shot_group, updatable_group, drawable_group)

    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    Shard.containers = (updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Powerup.containers = (powerup_group, updatable_group, drawable_group)
    asteroid_field = AsteroidField()

    world_audio.play(background_music, loops=-1)
    # Game Loop
    while game_start == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        text = font.render(f'{player.points}', True, "green")
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH /2, textRect.height)
        screen.blit(text, textRect)
        updatable_group.update(dt)
        for object in drawable_group:
            object.draw(screen)
        for asteroid in asteroid_group:
            if asteroid.collide(player) and player.invuln == False:
                death_audio.play(death_explosion)
                player.respawn()
                if player.lives == 0:
                    print("Game over!")
                    print(f"Score: {player.points}")
                    sys.exit()
            for shot in shot_group:
                if asteroid.collide(shot):
                    shot.kill()
                    player.score(1)
                    asteroid.split()
                    
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        #print(dt)

if __name__ == "__main__":
    main()