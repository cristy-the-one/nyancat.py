# Copyright 2012 Hajime Hikida
# Licensed under the Apache License 2.0

import sys
import pygame
from nyancat import Nyancat
from rainbow import Rainbow
from star_manager import StarManager

def main():
	pygame.init()
	pygame.display.set_caption("Nyan Cat")
	DISPLAY_SURFACE = pygame.display.set_mode((320, 240))
	BACKGROUND_COLOR = pygame.Color(15, 77, 143)
	DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
	FPS = 12
	CLOCK = pygame.time.Clock()
	
	#Create objects.
	cat = Nyancat()
	#cat = Nyancat(pygame.Rect(0, 0, 100, 100))
	#cat = Nyancat(pygame.Rect(0, 0, 200, 200))
	cat.rect.center = DISPLAY_SURFACE.get_rect().center
	rainbow = Rainbow(cat.rect, cat.cellSize)
	starManager = StarManager(DISPLAY_SURFACE.get_rect(), cat.cellSize, 20, -5)
	
	while True:
		DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
		
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		#Draw the objects. 
		#The objects will be drawn on the same surface object in the order they get called.
		rainbow.draw(DISPLAY_SURFACE)
		cat.draw(DISPLAY_SURFACE)
		starManager.draw(DISPLAY_SURFACE)
		
		#Update the animation state of the objects.
		rainbow.update()
		cat.update()
		starManager.update()
		
		pygame.display.update()
		CLOCK.tick(FPS)

if __name__ == "__main__":
	main()