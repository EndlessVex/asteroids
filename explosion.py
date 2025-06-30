import random
import pygame
from circleshape import *
from constants import *

class Shard(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, 5)
        self.lifespan = 0.3

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()
    