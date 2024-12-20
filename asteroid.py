import random
from circleshape import CircleShape
from constants import *
import contextlib
with contextlib.redirect_stdout(None):
	import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y* dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
             return
        random_angle = random.uniform(20,50)
        a_vector_1 = pygame.Vector2(self.velocity).rotate(-random_angle)
        a_vector_2 = pygame.Vector2(self.velocity).rotate(random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_asteriod_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteriod_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteriod_1.velocity = a_vector_1 * 1.2
        split_asteriod_2.velocity = a_vector_2 * 1.2