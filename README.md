# nyancat.py

Scalable Nyan Cat animation written in Python from scratch. [pygame](http://www.pygame.org/) required.

![Nyan Cat](/borealkiss/nyancat.py/raw/master/animation_examples/small.gif)

![Nyan Cat](/borealkiss/nyancat.py/raw/master/animation_examples/medium.gif)
	
![Nyan Cat](/borealkiss/nyancat.py/raw/master/animation_examples/large.gif)

## Example

The simplest implementation is here (note that half of the code is boilerplate for pygame):

	import pygame
	from nyancat import Nyancat
	from rainbow import Rainbow
	from star_manager import StarManager

	pygame.init()
	DISPLAY_SURFACE = pygame.display.set_mode((320, 240))
	BACKGROUND_COLOR = pygame.Color(15, 77, 143)
	DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
	FPS = 12
	CLOCK = pygame.time.Clock()
	
	#Create objects.
	cat = Nyancat(pygame.Rect(110, 90, 100, 250))
	rainbow = Rainbow(cat.rect, cat.pixelSize)
	stars = StarManager(DISPLAY_SURFACE.get_rect(), cat.pixelSize, 10)

	while True:
		DISPLAY_SURFACE.fill(BACKGROUND_COLOR)
		
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		#Draw the objects. 
		rainbow.draw(DISPLAY_SURFACE)
		cat.draw(DISPLAY_SURFACE)
		stars.draw(DISPLAY_SURFACE)
		
		#Update the animation state of the objects.
		rainbow.update()
		cat.update()
		stars.update()
		
		pygame.display.update()
		CLOCK.tick(FPS)

## License

The source code itself is provided under the terms of the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0). For the usage of the character, visit [http://nyan.cat/](http://nyan.cat/).

## Contact

* [http://blog.boreal-kiss.net/](http://blog.boreal-kiss.net/)
* [http://twitter.com/borealkiss](http://twitter.com/borealkiss)