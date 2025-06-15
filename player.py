from constants import *
import pygame
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def rotate(self, dt):        
        self.rotation += PLAYER_TURN_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.containers.add(shot)