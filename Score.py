import pygame, sys, math, time
from pygame.locals import *
if not pygame.font: print 'Warning, fonts disabled'
width = 900
height = 480
size = (width,height)

class Score():
    def init(self, value=0, pos = (width/2, height/2)):
        self.image = font.render(str(value), 1, (100,200,50))
        self.rect = self.image.get_rect()
        self.value = value
        self.place(pos)
    
    def place():
        self.rect.center = pt
        
    def increase(self, amount):
        self.value += amount
    
    def update():
        self.image = font.render(str(self.value), 1, (100,200,50))
       