from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import contextlib
with contextlib.redirect_stdout(None):
	import pygame


def main():
	# Initialising game
	pygame.init()

	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable)

	player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
	af = AsteroidField()
	# Create new clock object to maniuplate fps
	clock = pygame.time.Clock()
	# delta time to represent amount of time that has passed
	dt = 0
	# setting up screen
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		# allows user to quit by pressing "x" button on gui window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		# fills up screen with black colour
		screen.fill((0,0,0))
		# iterates over groups (makes codebase less cluttered)
		for obj in updateable:
			obj.update(dt)

		for obj in drawable:
			obj.draw(screen)
		# updates the full display to the screen 
		pygame.display.flip()
		# limits framerate to 60fps
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
