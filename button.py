import pygame, sys

#init stuff
pygame.init()
screen = pygame.display.set_mode((500,500))
gui_font = pygame.font.SysFont('inkfree',40)

class Button:
	def __init__(self,text,width,height,pos,elevation, colortop, colorbottom, hovertop, hoverbottom):
		#attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]

	  #colors
		self.button_top = colortop#'#6EB1EB'
		self.button_bottom = colorbottom
		self.hovertop = hovertop
		self.hoverbottom = hoverbottom
		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = self.button_top

		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = self.button_bottom
		#text
		self.text_surf = gui_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

	def draw(self): 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 

		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)

	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = self.hovertop
			self.bottom_color = self.hoverbottom
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					self.pressed = False
					return True
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = self.button_top
			self.bottom_color = self.button_bottom