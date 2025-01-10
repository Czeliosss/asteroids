import pygame
from constants import *
from player import *
def main():
	print("Starting asteroids!")
	#print(f"Screen width: {SCREEN_WIDTH}")
	#print(f"Screen height: {SCREEN_HEIGHT}")
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock()
	dt = 0

	#player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable,drawable)
	player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,PLAYER_RADIUS)

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
		#player.update(dt)
		#player.draw(screen)
		
		pygame.display.flip()
		

if __name__ == "__main__":
    	main()
