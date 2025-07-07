import pygame
from constants import *
from player import *
from bullet import *

class Powerup(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, type):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(position_x, position_y)
        self.type = type
        self.radius = 10
        self.despawn_timer = 0.0
        if self.type == 1:
            self.color = "blue"
        elif self.type == 2:
            self.color = "green"
        elif self.type == 3:
            self.color = "purple"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, width=2)

    def powerup_player(self, player):
        if self.type == 1:
            player.shield = True
            player.shield_timer = 0.0
            print("player got shield")
        elif self.type == 2:
            player.speedup = True
            player.speedup_timer = 0.0
        elif self.type == 3:
            player.triple_shot = True
            player.triple_timer = 0.0

    def update(self, dt):
        self.despawn_timer += dt
        if self.despawn_timer >= POWERUP_DESPAWN_RATE:
            self.kill()

    def collide(self, other):
        if self.position.distance_to(other.position) <= self.radius + other.radius:
            return True
        return False