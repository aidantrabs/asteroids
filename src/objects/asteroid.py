import pygame
import random

from src.constants import ASTEROID_MIN_RADIUS

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
            
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        old_radius = self.radius
        
        random_angle = random.uniform(20, 50)

        velocity_positive = self.velocity.copy().rotate(random_angle)
        velocity_negative = self.velocity.copy().rotate(-random_angle)

        new_radius = old_radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = velocity_positive * 1.2
        asteroid2.velocity = velocity_negative * 1.2
