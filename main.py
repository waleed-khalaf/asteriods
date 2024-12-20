from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from sys import exit
import contextlib
with contextlib.redirect_stdout(None):
	import pygame


def main():
	# Initialising game
	pygame.init()

	# setting up groups
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# putting objects into relevant groups
	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable)
	Shot.containers = (shots, updateable, drawable)

	# Instationting objects
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
		
		for obj in asteroids:
			if obj.hasCollided(player):
				exit("Game over!")

		for obj in asteroids:
			for shot in shots:
				if obj.hasCollided(shot):
					obj.split()

		for obj in drawable:
			obj.draw(screen)
		# updates the full display to the screen 
		pygame.display.flip()
		# limits framerate to 60fps
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
