import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import Shot

def main():
	print("Starting asteroids!")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	pygame.font.init()
	font = pygame.font.SysFont("Terminal", 12)

	#Pygame Groups
	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable,drawable)
	Asteroid.containers = (updatable,drawable, asteroids)
	AsteroidField.containers = (updatable,)
	Shot.containers = (updatable,drawable,shots)

	player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)
	asteroidfield = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		dt = clock.tick(60) / 1000

		for content in updatable:
			content.update(dt)
		for content in drawable:
			content.draw(screen)
		for content in asteroids:
			if player.check_collision(content):
				print("Collision! Exiting game")
				exit()
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.check_collision(shot):
					asteroid.split()
					shot.kill()

		#Leave flip last
		pygame.display.flip()
		

if __name__ == "__main__":
    	main()
