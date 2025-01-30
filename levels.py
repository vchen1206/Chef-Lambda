import pygame, sys
from button import Button
from lvl1 import *
from lvl2 import *
from lvl3 import *

#dimensions
width = 700
height = 700
#setup
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
white = '#FFFFFF'

balloons = Sprite("balloons",15,65,700/1.1, 700/1.1, "images/deco.png")
def level_screen():
	lvl1 = Button('Level 1',200,40,(width/2-100,170),5,'#6EB1EB','#659FD2','#7BE2F1','#74D1DF')
	lvl2 = Button('Level 2',200,40,(width/2-100,250),5,'#6EB1EB','#659FD2','#7BE2F1','#74D1DF')
	lvl3 = Button('Level 3',200,40,(width/2-100,330),5,'#6EB1EB','#659FD2','#7BE2F1','#74D1DF')
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		screen.fill(white)
		balloons.draw()
		lvl1.draw()
		if lvl1.check_click():
			print("lvl1 starting")
			start1()
		lvl2.draw()
		if lvl2.check_click():
			print("lvl2 starting")
			start2()
		lvl3.draw()
		if lvl3.check_click():
			print("lvl3 starting")
			start3()

		pygame.display.update()