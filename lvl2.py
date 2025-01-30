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

guacamole1 = Sprite("guac1",width/2-700/4,230,700/2, 700/2,"images/guac.png")
guacamole2 = Sprite("guac2",width/2-700/4,200,700/2, 700/2,"images/finishedguac.png")
def start2():
	counter, text = 6, '6'.rjust(3)
	pygame.time.set_timer(pygame.USEREVENT, 1000)
	font = pygame.font.SysFont('Consolas', 30)
	
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
		screen.blit(gui_font.render("ingredients for guacamole:", True, (0, 0, 0)), (32, 100))
		screen.blit(gui_font.render("avocado, tomato, onion, lemon/lime, ", True, (0, 0, 0)), (32, 150))
		screen.blit(gui_font.render("pepper", True, (0, 0, 0)), (32, 180))
		guacamole1.draw()
		pygame.display.update()

  
avocado = Sprite("avocado", 450,20,700/4,700/4, "images/avocado.png")
lemonandlime = Sprite("lemonandlime",width/2-310,60,700/3.5, 700/3.5, "images/lemonandlime.png")
onion = Sprite("onion", 40,260,503/2,569/2, "images/onion.png")
pepper = Sprite("pepper", 450,350,700/4, 700/4, "images/pepper.png")
tomato = Sprite("tomato",width/2-110,165,700/4, 700/4, "images/tomato.png")
cheese = Sprite("cheese", 275, 320, 700/4, 700/4, "images/cheese.png")
egg = Sprite("egg", 450,210,700/4, 700/4, "images/egg.png")
watermelon = Sprite("watermelon",width/2-100,1,700/3.5, 700/3.5, "images/watermelon.png")
imgs = [avocado, lemonandlime, onion, pepper, tomato, cheese, egg, watermelon]
def play():
  ingredients = ["avocado","lemonandlime","onion","pepper","tomato"]
  user_ingredients = []
  donebutton1 = Button('Done',200,40,(width/2-100,550),5,'#FEC150','#FDAE1C','#EB9F13','#E59500')
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
      print(user_ingredients)
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
	button1 = Button('Return',200,40,(width/2-100,120),5,'#FEC150','#FDAE1C','#EB9F13','#E59500')
	for i in range(len(imgs)):
		imgs[i].clicked = False
	while True:
	  for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		      pygame.quit()
		      sys.exit()

	  screen.fill(white)
	  if success:
	    guacamole2.draw()
	  result = "YUM! You made guacamole!" if success else "You failed :("
	  text0 = gui_font.render(result, True, '#000000', white)
	  rect0 = text0.get_rect()
	  rect0.center = (width/2, 50)
	  screen.blit(text0, rect0)
	  button1.draw()
	  if button1.check_click():
	    return

	  pygame.display.update()
	  clock.tick(60)