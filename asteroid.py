import pygame
import random
from circleshape import *
from constants import *
from player import Player
from explosion import Shard
from audio import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def split(self):
        asteroid_audio = pygame.mixer.find_channel()
        if asteroid_audio is not None:
            asteroid_audio.play(asteroid_explosion)
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
        self.shards(random.randint(3,5))

    def shards(self, num_of_shards):
        for shard in range(num_of_shards):
            shard_rand = self.velocity.rotate(random.uniform(0, 360))
            shard = Shard(self.position.x, self.position.y)
            shard.velocity = shard_rand *1.2
