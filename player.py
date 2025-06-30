from circleshape import *
from constants import *
from bullet import *

class Player(CircleShape):
    score = 0
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0.0
    
    # triangle is from boot.dev
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_timer <= 0:
            self.shot_timer = PLAYER_SHOOT_CONSTANT
            bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            bullet.velocity = forward * PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt

        if keys[pygame.K_w]:
            # right
            self.move(dt)
        
        if keys[pygame.K_a]:
            # left
            self.rotate(dt * -1)

        if keys[pygame.K_s]:
            # right
            self.move(dt * -1)

        if keys[pygame.K_d]:
            # right
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            # shoot
            self.shoot()