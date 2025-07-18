import pygame
import random
from asteroid import Asteroid
from constants import *
from powerups import *


class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.powerup_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def spawn_powerup(self, position_x, position_y, type):
        powerup = Powerup(position_x, position_y, type)
        print(f"spawned powerup at: {powerup.position} it is {powerup.color}")

    def update(self, dt):
        self.spawn_timer += dt
        self.powerup_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)

        if self.powerup_timer > POWERUP_SPAWN_RATE:
            self.powerup_timer = 0

            # spawning powerup randomly in screen
            self.spawn_powerup(random.randint(0 + POWERUP_WIDTH, SCREEN_WIDTH - POWERUP_WIDTH), random.randint(0 + POWERUP_HEIGHT, SCREEN_HEIGHT - POWERUP_HEIGHT), random.randint(1, POWERUP_KINDS))
            
