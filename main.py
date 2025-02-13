import pygame #from pygame.org - https://www.pygame.org/news
import sys
import random
import math
pygame.init()
scr_width = 1000
scr_height = 500
scr = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Rogue Like Platformer")
ticks = pygame.time.Clock()

class Surfaces(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,width,height,type):
        super(Surfaces,self).__init__()
        self.type = type
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        if self.type == "P":
            self.color = (128,128,128,255)
        elif self.type == "S":
            self.color = (255,0,0,255)
        else:
            self.color = (0,0,0,255)
        self.image = pygame.Surface((self.width,self.height),pygame.SRCALPHA)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center = (self.width*2,self.height*2))
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        self.objects_connected = []




test_platform = pygame.sprite.Group()
test_platform.add(Surfaces(1000,250,200,50,"P"))

run = True
while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scr.fill((255,255,255))
    
    test_platform.draw(scr)
    
    pygame.display.flip()
    ticks.tick(60)
pygame.quit()
sys.exit()