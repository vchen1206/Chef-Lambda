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

crepe1 = Sprite("crepe",width/2-700/4,270,700/2, 700/2, "images/crepe.png")
crepe2 = Sprite("crepe",width/2-700/3,220,700/1.5, 700/1.5, "images/finishedcrepe.png")
def start3():
	counter, text = 7, '7'.rjust(3)
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
		screen.blit(gui_font.render("ingredients for crepe:", True, (0, 0, 0)), (32, 100))
		screen.blit(gui_font.render("berries, butter, eggs, milk, flour ", True, (0, 0, 0)), (32, 150))
		screen.blit(gui_font.render("sugar, chocolate syrup", True, (0, 0, 0)), (32, 180))
		crepe1.draw()
		pygame.display.update()
    
#Sprite(name, x, y, x scale, y scale, filename)
berries = Sprite("berries",width/2-350,160,700/3.5, 700/3.5, "images/berries.png")
butter = Sprite("butter",width/2-20,210,700/3.5, 700/3.5, "images/butter.png")
watermelon = Sprite("watermelon",width/2+140,90,700/3.5, 700/3.5, "images/watermelon.png")
choco = Sprite("choco",width/2-190,190,700/3.5, 700/3.5, "images/chocolatesyrup.png")
flour = Sprite("flour",width/2-350,1,700/3.5, 700/3.5, "images/flour.png")
milk = Sprite("milk",width/2-160,1,700/3.5, 700/3.5, "images/milk.png")
cucumber = Sprite("cucumber",width/2+20,1,700/3.5, 700/3.5, "images/cucumber.png")
sugar = Sprite("sugar",width/2+120,350,700/3.5, 700/3.5, "images/sugar.png")
egg = Sprite("egg",width/2-30,380,700/4, 700/4, "images/egg.png")
tomato = Sprite("tomato",width/2-350,380,700/4, 700/4, "images/tomato.png")
avocado = Sprite("avocado",width/2-180,380,700/4, 700/4, "images/avocado.png")
imgs = [berries, butter, choco, flour, milk, cucumber, sugar, egg, tomato, avocado, watermelon]
def play():
  ingredients = ["berries", "butter", "choco", "egg","flour", "milk", "sugar"]
  user_ingredients = []
  donebutton1 = Button('Done',190,40,(width/2-100,570),5,'#F8B9CE','#F6ADC5','#E785A5','#E6618D')

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
	button1 = Button('Return',200,40,(width/2-100,120),5,'#F8B9CE','#F6ADC5','#E785A5','#E6618D')
	for i in range(len(imgs)):
		imgs[i].clicked = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		screen.fill(white)
		if success:
			crepe2.draw()
		result = "YUM! You made crepe!" if success else "You failed :("
		text0 = gui_font.render(result, True, '#000000', white)
		rect0 = text0.get_rect()
		rect0.center = (width/2, 50)
		screen.blit(text0, rect0)
		button1.draw()
		if button1.check_click():
			return

		pygame.display.update()
		clock.tick(60)