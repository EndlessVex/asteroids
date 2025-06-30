import pygame
import random
from circleshape import *
from constants import *
from player import Player
from explosion import Shard

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.explode()
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

    def explode(self):
        shard1_rand = self.velocity.rotate(random.uniform(0, 360))
        shard2_rand = self.velocity.rotate(random.uniform(0, 360))
        shard3_rand = self.velocity.rotate(random.uniform(0, 360))
        shard1 = Shard(self.position.x, self.position.y)
        shard2 = Shard(self.position.x, self.position.y)
        shard3 = Shard(self.position.x, self.position.y)
        shard1.velocity = shard1_rand *1.2
        shard2.velocity = shard2_rand *1.2
        shard3.velocity = shard3_rand *1.2