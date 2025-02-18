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
    def activate(self):
        if len(self.objects_connected) > 0:
            if self.type == "DOOR":
                print("pp")
                for i in self.objects_connected:
                    self.objects_connected[i].rect.centerx = 500
                    self.objects_connected[i].rect.centery = 275

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
        elif (self.jumping == True) and (self.collide_up == True):
            self.jumping = False
            self.active_jump = False   
    def collide(self,group):
        left_collided = 0
        right_collided = 0
        up_collided = 0
        down_collided = 0
        for obj in group:
            if obj.rect.collidepoint(self.rect.centerx-self.width/2+1,self.rect.centery):
                left_collided += 1
                if self not in obj.objects_connected:
                    print("pppp")
                    obj.objects_connected.append(self)
            else:
                try:
                    obj.objects_connected.remove(self)
                except:
                    pass
            if obj.rect.collidepoint(self.rect.centerx+self.width/2-1,self.rect.centery):
                right_collided += 1
                if self not in obj.objects_connected:
                    obj.objects_connected.append(self)
            else:
                try:
                    obj.objects_connected.remove(self)
                except:
                    pass
            if obj.rect.collidepoint(self.rect.centerx,self.rect.centery-self.height/2+1):
                up_collided += 1
                if self not in obj.objects_connected:
                    obj.objects_connected.append(self)
            else:
                try:
                    obj.objects_connected.remove(self)
                except:
                    pass
            if obj.rect.collidepoint(self.rect.centerx,self.rect.centery+self.height/2-1):
                down_collided +=1
                if self not in obj.objects_connected:
                    obj.objects_connected.append(self)
            else:
                try:
                    obj.objects_connected.remove(self)
                except:
                    pass
        if left_collided == 0:
            self.collide_left = False
        else:
            self.collide_left = True
        if right_collided == 0:
            self.collide_right = False
        else:
            self.collide_right = True
        if up_collided == 0:
            self.collide_up = False
        else:
            self.collide_up = True
        if down_collided == 0:
            self.collide_down = False
        else:
            self.collide_down = True
    def gravity(self):
        if (self.jumping == False) and (self.collide_down == False):
            self.rect.centery += self.grav_amt
            self.grav_amt += self.grav_inc
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

ply=pygame.sprite.Group()
ply.add(Player(100,300,50,100))

run = True
while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scr.fill((255,255,255))
    
    for player in ply:
        player.collide(pp.room_surfaces)
        player.move(keys)
        player.gravity()

    ply.draw(scr)


    # test_platform.draw(scr)

    for plat in pp.room_surfaces:
        plat.activate()

    pp.room_surfaces.draw(scr)

    pygame.display.flip()
    ticks.tick(60)
pygame.quit()
sys.exit()