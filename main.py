import pygame, sys
from button import Button
from sprites import *
from lvl1 import *
from lvl2 import *
from lvl3 import *
from levels import *

pygame.init()

#dimensions
width = 700  #1200
height = 700

#setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chef Lambda')
clock = pygame.time.Clock()
gui_font = pygame.font.SysFont('georgia', 30)

#colors
nice_blue = (78, 151, 215)
white = '#FFFFFF'
black = '#000000'

button1 = Button('Play', 200, 40, (width / 2 - 100, 120), 5, '#F8B9CE',
                 '#F6ADC5', '#F25086', '#F04880')
guacamole2 = Sprite("guac2", width / 2 - 300, 410, 700 / 2.5, 700 / 2.5,
                    "images/finishedguac.png")
crepe2 = Sprite("crepe", width / 2 + 10, 450, 700 / 2.5, 700 / 2.5,
                "images/finishedcrepe.png")
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)
    #guacamole2.draw()
    #crepe2.draw()
    mouse = pygame.mouse.get_pos()

    #beginning button
    button1.draw()
    if button1.check_click():
        level_screen()

    chef = Chef(width / 2 - 503 / 4, 220, 503 / 2, 569 / 2)
    chef.draw()

    #text - words, text, highlight
    text0 = gui_font.render('Welcome to Chef Lambda', True, black, white)
    rect0 = text0.get_rect()
    rect0.center = (width / 2, 50)
    screen.blit(text0, rect0)

    pygame.display.update()
    clock.tick(60)
