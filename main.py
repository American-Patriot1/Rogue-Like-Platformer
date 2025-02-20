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
placeholder=[]
rooom2=[
    [["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["D",1,[placeholder,[8,16]]],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"]]
]
#11x17
rooom1=[
    [["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["S"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["D",1,[rooom2,[8,0]]]],
    [["S"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"],["_"]],
    [["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"],["S"]]
]
rooom2[8][0][2][0] = rooom1
class Room(pygame.sprite.Sprite):
    def __init__(self,room_grid):
        super(Room,self).__init__()
        self.room_grid=room_grid
        self.room_surfaces=pygame.sprite.Group()
        self.door_locs = []
        for y in range(11):
            for x in range(20):
                #i could change it so it is like the door and the width and height are stored in the list
                if room_grid[y][x][0]=="S":
                    self.room_surfaces.add(Surfaces(25+(50*x),25+(50*y),50,50,"SURFACE",[-1,[0,0]]))
                elif room_grid[y][x][0]=="D":
                    self.door_locs.append([self.room_grid[y][x][1],[self.room_grid,[y,x]],[self.room_grid[y][x][2][0],self.room_grid[y][x][2][1]]])
                    self.room_surfaces.add(Surfaces(25+(50*x),25+(50*y),50,150,"DOOR",[self.dooddr_locs[-1][0],self.door_locs[-1][1][1]]))
                    #when generating the maze make a overarching door_locs, 
                    #make the 2nd slot and 3rd slot both lists that are 2 in length and contain first the room and 2nd a list with the location
                    #and check if the door number already exsists
                    
                    
class Surfaces(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,width,height,type,door_info):
        super(Surfaces,self).__init__()
        self.type = type
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.door_id = door_info
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
    def activate(self):
        if self.objects_connected != []:
            if self.type == "DOOR":
                switch_room(self.door_id)
class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,width,height):
        super(Player,self).__init__()
        self.color=(255,0,0,255)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width,self.height), pygame.SRCALPHA)
        pygame.draw.circle(self.image,self.color,(self.width/2,self.height/2),self.width)
        self.rect=self.image.get_rect(center=(self.width*2,self.height*2))
        self.rect.centerx = pos_x
        self.rect.centery = pos_y
        self.jump_amt = 0
        self.jumping = False
        self.active_jump = False
        self.grav_amt = 1
        self.grav_inc = 0.25
        self.collided = False
        self.collide_left = False
        self.collide_right = False
        self.collide_down = False
        self.collide_up = False
        self.health = 100
    def move(self,keys):
        if (keys[pygame.K_a]) and (self.collide_left == False):
            self.rect.centerx -= 10
        if (keys[pygame.K_d]) and (self.collide_right == False):
            self.rect.centerx += 10
        if (keys[pygame.K_SPACE]) and (self.collide_up == False):
            if (self.collide_down == True):
                self.grav_amt = 1
                self.jump_amt = 20
                self.jumping = True
                self.active_jump = True
                self.rect.centery -= self.jump_amt
                self.jump_amt -= self.grav_amt
            elif (self.active_jump == True) and (self.jumping == True):
                self.rect.centery -= self.jump_amt
                self.jump_amt -= self.grav_amt
                if self.jump_amt <= 0:
                    self.jumping = False
            elif (self.jumping == True):
                self.active_jump = False
                self.rect.centery -= self.jump_amt
                self.jump_amt -= self.grav_amt*2
                if self.jump_amt <= 0:
                    self.jumping = False
        elif (self.jumping == True) and (self.collide_up == False):
            self.active_jump = False
            self.rect.centery -= self.jump_amt
            self.jump_amt -= self.grav_amt*2
            if self.jump_amt <= 0:
                self.jumping = False
    def collide(self,group):
        self.collide_left = False
        self.collide_right = False
        self.collide_up = False
        self.collide_down = False
        self.collided = False
        for obj in group:
            cld = False
            #left
            if obj.rect.collidepoint(self.rect.centerx-self.width/2-2,self.rect.centery):
                self.collide_left = True
                cld = True
            #right
            if obj.rect.collidepoint(self.rect.centerx+self.width/2+2,self.rect.centery):
                self.collide_right = True
                cld = True
            #up
            if obj.rect.collidepoint(self.rect.centerx,self.rect.centery-self.height/2-2):
                self.collide_up = True
                cld = True
                self.jumping = False
                self.active_jump = False   
            #down
            if obj.rect.collidepoint(self.rect.centerx,self.rect.centery+self.height/2+2):
                self.collide_down = True
                cld = True
                self.grav_amt = 1
            if cld == True:
                self.collided = True
                if self not in obj.objects_connected:
                    obj.objects_connected.append(self)
            elif self in obj.objects_connected:
                obj.objects_connected.remove(self)
    def gravity(self):
        if (self.jumping == False) and (self.collide_down == False):
            self.rect.centery += self.grav_amt
            self.grav_amt += self.grav_inc
def switch_room(door_num):
    # if active_room == r1:
    #    active_room = r2 
    # elif active_room == r1:
    #    active_room = r2
    active_room = r2
    for y in len(active_room.room_grid):
        for x in len(active_room.room_grid[y]):
            if (active_room.room_grid[y][x][0]=="D") and (active_room.room_grid[y][x][1]==door_num):
                for p in ply:
                    if x==0:
                        p.rect.centerx=75+(50*x)
                        p.rect.centery=25+(50*y)
                    elif x==16:
                        p.rect.centerx=75+(50*x)
                        p.rect.centery=25+(50*y)
r1 = Room(rooom1)
r2 = Room(rooom2)

active_room = r1

ply = pygame.sprite.Group()
ply.add(Player(100,300,50,100))

run = True
while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scr.fill((255,255,255))
    
    active_room.room_surfaces.draw(scr)

    for player in ply:
        player.collide(active_room.room_surfaces)
        player.move(keys)
        player.gravity()

    ply.draw(scr)


    # test_platform.draw(scr)

    for plat in active_room.room_surfaces:
        for player in ply:
            if player.collided == True:
                plat.activate()

    pygame.display.flip()
    ticks.tick(60)
pygame.quit()
sys.exit()