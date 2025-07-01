import pygame
from circleshape import *
from constants import *
from bullet import *
from audio import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0.0
        self.respawn_timer = 0.0
        self.blink_timer = 0.0
        self.points = 0
        self.lives = 3
        self.respawned = False
        self.invuln = False
        self.blinking = False
        self.vel = pygame.Vector2(0, 0)
        self.input = False
    
    # triangle is from boot.dev
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        if self.blinking == True:
            pygame.draw.polygon(screen, "red", self.triangle(), width=2)
        if self.blinking == False:
            pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def accelerate(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.vel += forward * PLAYER_ACCELERATION * dt
        if self.vel.length() > PLAYER_SPEED:
            self.vel.scale_to_length(PLAYER_SPEED)

    def apply_friction(self, dt):
        if self.vel.length() > 0:
            friction_force = PLAYER_FRICTION * dt
            if friction_force > self.vel.length():
                self.vel = pygame.Vector2(0, 0)
            else:
                self.vel -= self.vel.normalize() * friction_force

    def move(self, dt):
        self.position += self.vel * dt
        
        
    def shoot(self):
        if self.shot_timer <= 0:
            self.shot_timer = PLAYER_SHOOT_CONSTANT
            player_audio.play(shoot_sound)
            bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            bullet.velocity = forward * PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt
        self.blink(dt)

        if self.respawned == True:
            self.respawn_timer += dt
            if self.respawn_timer > PLAYER_RESPAWN_TIME:
                self.respawn_timer = 0
                self.respawned = False
                self.invuln = False
                self.vel = pygame.Vector2(0, 0)

        if keys[pygame.K_w]:
            # forward
            self.accelerate(dt)
            self.input = True

        if keys[pygame.K_a]:
            # left
            self.rotate(dt * -1)

        if keys[pygame.K_s]:
            # backwards
            self.accelerate(dt * -0.5)
            self.input = True

        if keys[pygame.K_d]:
            # right
            self.rotate(dt, )

        if keys[pygame.K_SPACE]:
            # shoot
            if self.lives != 0:
                self.shoot()

        if not self.input:
            self.apply_friction(dt)

        self.move(dt)
        self.input = False

    def respawn(self):
        self.lives -= 1
        self.invuln = True
        self.respawned = True
        self.position = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    def score(self, points):
        self.points += points

    def blink(self, dt):
        if self.invuln:
            self.blink_timer += dt
            if self.blink_timer > PLAYER_BLINK_TIME:
                self.blink_timer = 0
                self.blinking = not self.blinking
        else: self.blinking = False