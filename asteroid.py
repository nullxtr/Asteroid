import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
         pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        asteroid_fragment_radius = self.radius - ASTEROID_MIN_RADIUS

        first_part_velocity = self.velocity.rotate(random_angle)
        second_part_velocity = self.velocity.rotate(-random_angle)

        first_part = Asteroid(self.position.x, self.position.y, asteroid_fragment_radius)
        second_part = Asteroid(self.position.x, self.position.y, asteroid_fragment_radius)
        
        first_part.velocity = first_part_velocity * 1.2
        second_part.velocity = second_part_velocity * 1.2
