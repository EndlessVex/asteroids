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

    def power_type(self):
        if self.type == 1:
            pass # Shield
        elif self.type == 2:
            pass # Speed Up
        elif self.type == 3:
            pass # triple shot

    def update(self, dt):
        self.despawn_timer += dt
        if self.despawn_timer >= POWERUP_DESPAWN_RATE:
            self.kill()