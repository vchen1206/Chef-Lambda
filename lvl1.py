import pygame, sys
from button import Button
from sprites import *

#dimensions
width = 700
height = 700

#setup
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

white = '#FFFFFF'
black = '#000000'
gui_font = pygame.font.SysFont('georgia',30)

cucumberroll1 = Sprite("cucumber1",width/2-700/4,250,700/2, 700/2, "images/sushi.png")
cucumberroll2 = Sprite("cucumber2", width/2-700/4, 250, 700/2, 700/2, "images/finishedsushi.png")
def start1():
	counter, text = 5, '5'.rjust(3)
	pygame.time.set_timer(pygame.USEREVENT, 1000)
	font = pygame.font.SysFont('comicsansms', 30)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.USEREVENT: 
				counter -= 1
				if counter > 0:
					text = str(counter).rjust(3)
				else:
					play()
					return
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		screen.fill(white)
		screen.blit(font.render(text, True, (0, 0, 0)), (32, 50))
		screen.blit(gui_font.render("ingredients for cucumber sushi:", True, (0, 0, 0)), (32, 100))
		screen.blit(gui_font.render("cucumber, rice, seaweed", True, (0, 0, 0)), (32, 150))
		cucumberroll1.draw()
		pygame.display.update()


cucumber = Sprite("cucumber", 400,5,503/2,569/2, "images/cucumber.png")
rice = Sprite("rice", 1,260,503/2,569/2, "images/rice.png")
seaweed = Sprite("seaweed", 450,270,503/2,569/2, "images/seaweed.png")
egg = Sprite("egg",width/2-110,70,700/4, 700/4, "images/egg.png")
tomato = Sprite("tomato",width/2-310,60,700/3.5, 700/3.5, "images/tomato.png")
fish = Sprite("fish", width/2-150,250, 700/2.5, 700/2.5, "images/fish.png")
imgs = [cucumber, rice, seaweed, egg, tomato, fish]
def play():
  ingredients = ["cucumber", "rice", "seaweed"]
  user_ingredients = []
  donebutton1 = Button('Done',200,40,(width/2-100,570),5,'#ACE185','#A4D481','#87E343','#80D245')

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    screen.fill(white)
    for i in range(len(imgs)):
      imgs[i].draw()
      if imgs[i].check_click():
        user_ingredients.append(imgs[i].name)
    
    donebutton1.draw()
    if donebutton1.check_click():
      final = []
      for i in user_ingredients: 
        if i not in final: 
          final.append(i) 
      final.sort()
      print(final)
      #check to see if user got right ingredients
      if final == ingredients:
        result(True)
      else:
        result(False)
      return
    pygame.display.update()
    clock.tick(60)


def result(success):
	button1 = Button('Return',200,40,(width/2-100,120),5,'#ACE185','#A4D481','#87E343','#80D245')
	for i in range(len(imgs)):
		imgs[i].clicked = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		screen.fill(white)
		if success:
			cucumberroll2.draw()			
		result = "YUM! You made cucumber sushi!" if success else "You failed :("
		text0 = gui_font.render(result, True, '#000000', white)
		rect0 = text0.get_rect()
		rect0.center = (width/2, 50)
		screen.blit(text0, rect0)
		button1.draw()
		if button1.check_click():
			return

		pygame.display.update()
		clock.tick(60)