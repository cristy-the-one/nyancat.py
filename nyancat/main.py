#!/usr/bin/env python

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
	cat = Nyancat(pygame.Rect(110, 90, 100, 250))
	rainbow = Rainbow(cat.rect, cat.pixelSize)
	starManager = StarManager(10, DISPLAY_SURFACE, cat.pixelSize)
	
	#count = 0
	
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
		cat.update()
		starManager.update(DISPLAY_SURFACE)
		
		#Update the animation frame of the rainbow object only when the cat object is in the initiali state, i.e., in the first frame.
		#This is becaue the cat has 6 frames while the rainbow only 2.
		if cat.initialState:
			rainbow.update()
		
		#pygame.image.save(DISPLAY_SURFACE, "nyancat_animation_" + str(count) + ".png")
		#count += 1	
		
		pygame.display.update()
		CLOCK.tick(FPS)

if __name__ == "__main__":
	main()