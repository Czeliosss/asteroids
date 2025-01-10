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
	score = 0

	pygame.font.init()
	font = pygame.font.SysFont("Terminal", FONT_SIZE)

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
				print(f"Score: {int(score)}")
				exit()
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.check_collision(shot):
					asteroid.split()
					shot.kill()
					score = score + asteroid.add_score()

		#Leave flip last
		clear_score_area(screen)
		render_score(screen, int(score), font, (10,10))
		pygame.display.flip()


def render_score(screen, score, font, position):
		score_text = f"Score: {score}"
		score_surface = font.render(score_text, True, "white")
		screen.blit(score_surface, position)

def clear_score_area(screen):
	rect = pygame.Rect(0,0, 200, 50)
	pygame.draw.rect(screen, (0,0,0), rect)

if __name__ == "__main__":
    	main()
