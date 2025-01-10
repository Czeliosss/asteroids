import pygame
import random
import math
from circleshape import *
from constants import *
class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.has_split_times = 0
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
	def update(self, dt):
		self.position += self.velocity * dt
	def split(self):
		
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else: 
			angle = random.uniform(20, ASTEROID_MAX_SPLIT_RANGE)
			velocity1 = self.velocity.rotate(angle)
			velocity2 = self.velocity.rotate(-angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
			new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
			new_asteroid1.velocity = velocity1 * ASTEROID_SPEED_MULTIPLIER
			new_asteroid2.velocity = velocity2 * ASTEROID_SPEED_MULTIPLIER
			new_asteroid1.has_split_times = self.has_split_times + 1
			new_asteroid2.has_split_times = self.has_split_times + 1
	def add_score(self):
		return 1 + self.has_split_times * SCORE_MULTIPLIER_PER_SPLIT