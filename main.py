#!/usr/bin/env python

import sys
import random
import pygame
from nyancat.nyancat import Nyancat
from nyancat.rainbow import Rainbow
from nyancat.star import Star

def main():
	pygame.init()
	pygame.display.set_caption("Nyan Cat")
	DISPLAY_SURFACE = pygame.display.set_mode((320, 240))
	BACKGROUND_COLOR = pygame.Color(15, 77, 143)
	DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
	FPS = 12
	CLOCK = pygame.time.Clock()
	
	cat = Nyancat(pygame.Rect(110, 90, 100, 250))
	rainbow = Rainbow(cat.rect, cat.pixelSize)
	stars = createStars(10, DISPLAY_SURFACE, cat.pixelSize)

	while True:
		DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
		
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
				
		rainbow.draw(DISPLAY_SURFACE)
		cat.draw(DISPLAY_SURFACE)
		drawStars(stars, DISPLAY_SURFACE)
		
		cat.update()
		
		if cat.initialState:
			rainbow.update()
		
		updateStars(stars, DISPLAY_SURFACE, cat.pixelSize)
				
		pygame.display.update()
		CLOCK.tick(FPS)

def createStars(numStars, surface, pixelSize):
	stars = []
			
	for i in range(numStars):
		star = createStar(surface, pixelSize)
		stars.append(star)
			
	return stars

def createStar(surface, pixelSize):
	surfRect = surface.get_rect()
	x = random.randint(surfRect.left, surfRect.width)
	y = random.randint(surfRect.top, surfRect.height)
	star = Star(pixelSize)
	star.rect.topleft = (x, y)
	return star

def updateStars(stars, surface, pixelSize):
	STAR_VELOCITY = -10
	
	for i in reversed(range(len(stars))):
		star = stars[i]
		star.rect.left += STAR_VELOCITY
		star.update()
		
		if star.animationFinished:
			stars.remove(star)
			newStar = createStar(surface, pixelSize)
			newStar.currentFrame = 0
			stars.append(newStar)

def drawStars(stars, surface):
	for star in stars:
		star.draw(surface)	
	
if __name__ == "__main__":
	main()