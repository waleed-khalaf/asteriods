from constants import *
from player import Player
import contextlib
with contextlib.redirect_stdout(None):
	import pygame


def main():
	# Initialising game
	pygame.init()
	player_1 = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
	
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

		player_1.draw(screen)
		# updates the full display to the screen 
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
