#!/usr/bin/env python

import pygame
import sys
from nyancat.nyancat import Nyancat

def main():
	pygame.init()
	DISPLAY_SURFACE = pygame.display.set_mode((350, 250))
	BACKGROUND_COLOR = pygame.Color(15, 77, 143)
	DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
	FPS = 12
	CLOCK = pygame.time.Clock()
	
	#cat = Nyancat()
	cat = Nyancat(pygame.Rect(0, 0, 350, 250))
	
	while True:
		DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
		
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				
		cat.draw(DISPLAY_SURFACE)
		cat.update()		
				
		pygame.display.update()
		CLOCK.tick(FPS)
		
if __name__ == "__main__":
	main()