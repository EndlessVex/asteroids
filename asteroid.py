import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        pos_rand = self.velocity.rotate(angle)
        neg_rand = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        pos_baby = Asteroid(self.position.x, self.position.y, new_radius)
        neg_baby = Asteroid(self.position.x, self.position.y, new_radius)
        pos_baby.velocity = pos_rand *1.2
        neg_baby.velocity = neg_rand *1.2

    def update(self, dt):
        self.position += self.velocity * dt