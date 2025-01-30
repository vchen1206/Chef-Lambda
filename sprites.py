import pygame, sys

#dimensions
width = 700
height = 700

#setup
screen = pygame.display.set_mode((width,height))
class Chef(pygame.sprite.Sprite):
	def __init__(self, x, y, x_scale, y_scale):
		self.image = pygame.image.load("images/betterchef.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.xs = x_scale
		self.ys = y_scale

	def moveRight(self, pixels):
		self.x += pixels
	def moveLeft(self, pixels):
		self.x -= pixels
	def moveDown(self, pixels):
		self.y += pixels
	def moveUp(self, pixels):
		self.y -= pixels

	def draw(self):
		self.image = pygame.transform.scale(self.image, (self.xs,self.ys)) #scale image
		screen.blit(self.image, (self.x,self.y))

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		return pygame.mouse.get_pressed()[0] and self.x<=mouse_pos[0]<=self.x+self.xs and self.y<= mouse_pos[1] <= self.y+self.ys

class Sprite(pygame.sprite.Sprite):
	def __init__(self, name, x, y, x_scale, y_scale, filename):
		self.image = pygame.image.load(filename).convert_alpha()
		self.rect = self.image.get_rect()
		self.x = x
		self.y = y
		self.xs = x_scale
		self.ys = y_scale
		self.clicked = False
		self.name = name

	def moveRight(self, pixels):
		self.x += pixels
	def moveLeft(self, pixels):
		self.x -= pixels
	def moveDown(self, pixels):
		self.y += pixels
	def moveUp(self, pixels):
		self.y -= pixels


	def draw(self):
		self.image = pygame.transform.scale(self.image, (self.xs,self.ys)) #scale image
		screen.blit(self.image, (self.x,self.y)) 
		if self.clicked:
			check = pygame.image.load("images/checkmark.png").convert_alpha()
			check = pygame.transform.scale(check, (256/2,256/2))
			screen.blit(check, (self.x+70, self.y+20))

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if pygame.mouse.get_pressed()[0] and self.x<=mouse_pos[0]<=self.x+self.xs and self.y<= mouse_pos[1] <= self.y+self.ys:
			self.clicked = True
			return True
		else:
			return False