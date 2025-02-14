import pygame #from pygame.org - https://www.pygame.org/news
import sys
import random
import math
pygame.init()
scr_width = 1000
scr_height = 550
scr = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Rogue Like Platformer")
ticks = pygame.time.Clock()
rooom=[
    [["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["D"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"]]
]
class Room(pygame.sprite.Sprite):
    def __init__(self,room_grid):
        super(Room,self).__init__()
        self.room_grid=room_grid
        self.room_surfaces=pygame.sprite.Group()
        for y in range(11):
            for x in range(20):
                #i could change it so it is like the door and the width and height are stored in the list
                if rooom[y][x][0]=="S":
                    self.room_surfaces.add(Surfaces(25+(50*x),25+(50*y),50,50,"SURFACE"))
                elif rooom[y][x][0]=="D":
                    self.room_surfaces.add(Surfaces(25+(50*x),25+(50*y),50,150,"DOOR"))

class Surfaces(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,width,height,type):
        super(Surfaces,self).__init__()
        self.type = type
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        if self.type == "SURFACE":
            self.color = (128,128,128,255)
        elif self.type == "SPIKE":
            self.color = (255,0,0,255)
        elif self.type == "DOOR":
            self.color = (0,0,255,255)
        else:
            self.color = (0,0,0,255)
        self.image = pygame.Surface((self.width,self.height),pygame.SRCALPHA)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center = (self.width*2,self.height*2))
        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y
        self.objects_connected = []

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        pass


# test_platform = pygame.sprite.Group()
# test_platform.add(Surfaces(500,525,1000,50,"SURFACE"))
# test_platform.add(Surfaces(500,25,1000,50,"SURFACE"))
# #wall
# test_platform.add(Surfaces(25,200,50,300,"SURFACE"))
# test_platform.add(Surfaces(975,200,50,300,"SURFACE"))
# #door
# test_platform.add(Surfaces(25,425,50,150,"DOOR"))
# test_platform.add(Surfaces(975,425,50,150,"DOOR"))

# clr="SPIKE"
# for y in range(9):
#     if clr=="SPIKE":
#         clr=""
#     else:
#         clr="SPIKE"
#     for x in range(18):
#         test_platform.add(Surfaces(75+(50*(x)),(75+(50*(y))),50,50,clr))
#         if clr=="SPIKE":
#             clr=""
#         else:
#             clr="SPIKE"
        
pp=Room(rooom)

run = True
while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scr.fill((255,255,255))
    
    # test_platform.draw(scr)

    pp.room_surfaces.draw(scr)

    pygame.display.flip()
    ticks.tick(60)
pygame.quit()
sys.exit()