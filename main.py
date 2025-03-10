import pygame #from pygame.org - https://www.pygame.org/news
import sys# from https://docs.python.org/3/library/sys.html
pygame.init()
scr_width = 1000
scr_height = 550
scr = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Rogue Like Platformer")
ticks = pygame.time.Clock()

class Maze(pygame.sprite.Sprite):
    def __init__(self,min_rooms,max_doors,player):
        super(Maze,self).__init__()
        self.maze=pygame.sprite.Group()
        room_id=0
        total_doors=0
        self.player=player
        unended_doors=[]
        count=1
        while ((min_rooms!=0) or (len(unended_doors)!=0)) and (count<=2):
            if min_rooms==0:
                max_doors=1
            door_locs = [[2,0],[5,0],[8,0],[2,19],[5,19],[8,19]]
            if room_id == 0:
                door_locs = [[5,19]]
            amt_of_doors=0
            fixed_door = False
            room=[]
            door_holdover=[]
            created_new_door=False
            for y in range(11):
                room.append([])
                for x in range(20):
                    room[y].append([])
                    if [y,x] in door_holdover:
                        door_holdover.remove([y,x])
                        room[y][x].append("_")
                    elif (len(unended_doors)!=0) and (fixed_door == False) and (created_new_door==False):
                        for i in range(len(unended_doors)):
                            if [y,x] in unended_doors[i]:
                                room[y][x].append("D")
                                room[y][x].append(unended_doors[i][1])
                                room[y][x].append(unended_doors[i][2])
                                room[y-1][x].append("_")
                                door_holdover.append([y+1,x])
                                if x==0:
                                    side=19
                                else:
                                    side=0
                                for b in self.maze:
                                    if b.id==unended_doors[i][2]:
                                        b.room_grid[y][side][2]=room_id
                                        for a in b.room_surfaces:
                                            try:
                                                a.other_room=room_id
                                            except:
                                                pass
                                fixed_door=True
                                unended_doors.pop(i)
                                amt_of_doors+=1
                                door_locs.remove([y,x])
                            elif ((y == 0) or (y== 10)) and (room[y][x] == []):
                                room[y][x].append("S")
                            elif ((x == 0) or (x==19)) and (room[y][x] == []):
                                room[y][x].append("S")
                            elif  (room[y][x] == []):
                                room[y][x].append("_")
                    elif (min_rooms>0) and ([y,x] in door_locs) and (amt_of_doors < max_doors):
                        if ((fixed_door==False) and (len(unended_doors)==0)) or ((fixed_door==True) and ((len(unended_doors)==0) or ((max_doors-amt_of_doors)>=1))):
                            room[y][x].append("D")
                            room[y][x].append(total_doors)
                            room[y][x].append(room_id)
                            room[y-1][x][0]="_"
                            door_holdover.append([y+1,x])
                            [y-1,x]
                            if x==0:
                                side=19
                            else:
                                side=0
                            unended_doors.append([[y,side],total_doors,room_id])
                            amt_of_doors += 1
                            total_doors += 1
                            created_new_door=True
                        elif ((y == 0) or (y== 10)) and (room[y][x] == []):
                            room[y][x].append("S")
                        elif ((x == 0) or (x==19)) and (room[y][x] == []):
                            room[y][x].append("S")
                        elif  (room[y][x] == []):
                            room[y][x].append("_")
                    elif ((y == 0) or (y== 10)) and (room[y][x] == []):
                        room[y][x].append("S")
                    elif ((x == 0) or (x==19)) and (room[y][x] == []):
                        room[y][x].append("S")
                    elif  (room[y][x] == []):
                        room[y][x].append("_")
                    else:
                        room[y][x].append("_")
            self.maze.add(Room(room,room_id))
            room_id+=1
            min_rooms+=1
            count+=1
        self.active_room=0
    def switch_room(self,id,room):
        for r in self.maze:
            if r.id==room:
                for y in range(len(r.room_grid)):
                    for x in range(len(r.room_grid[y])):
                        if (r.room_grid[y][x][0]=="D") and (r.room_grid[y][x][1]==id):
                            if x==0:
                                self.player.rect.centerx=80+(50*x)
                                self.player.rect.centery=25+(50*y)
                            elif x==19:
                                self.player.rect.centerx=-30+(50*x)
                                self.player.rect.centery=25+(50*y)
                            self.active_room=room
    def determine_active_room(self):
        for r in self.maze:
            if r.id==self.active_room:
                return r
            
class Room(pygame.sprite.Sprite):
    def __init__(self,room_grid,id):
        super(Room,self).__init__()
        self.room_grid=room_grid
        self.room_surfaces=pygame.sprite.Group()
        self.id=id
        for y in range(len(room_grid)):
            for x in range(len(room_grid[y])):
                if room_grid[y][x][0]=="S":
                    self.room_surfaces.add(Surfaces(25+(50*x),25+(50*y),50,50,"SURFACE",-1,self.id))
                elif room_grid[y][x][0]=="D":
                    self.room_surfaces.add(Surfaces(25+(50*x),25+(50*y),50,150,"DOOR",[self.room_grid[y][x][1],self.room_grid[y][x][2]],self.id))
                    
class Surfaces(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,width,height,type,door_info,room_in):
        super(Surfaces,self).__init__()
        self.room_in=room_in
        self.type = type
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        if door_info!=-1:
            self.door_id=door_info[0]
            self.other_room=door_info[1]
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
                maze1.switch_room(self.door_id,self.other_room)
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
            if obj.rect.collidepoint(self.rect.centerx-self.width/2-2,self.rect.centery):
                self.collide_left = True
                cld = True
            if obj.rect.collidepoint(self.rect.centerx+self.width/2+2,self.rect.centery):
                self.collide_right = True
                cld = True
            if obj.rect.collidepoint(self.rect.centerx,self.rect.centery-self.height/2-2):
                self.collide_up = True
                cld = True
                self.jumping = False
                self.active_jump = False   
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

ply = pygame.sprite.Group()
ply.add(Player(100,300,50,100))

for p in ply:
    maze1 = Maze(2,1,p)

run = True
while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    scr.fill((255,255,255))
    
    act_room=maze1.determine_active_room()

    act_room.room_surfaces.draw(scr)

    for player in ply:
        player.collide(act_room.room_surfaces)
        player.move(keys)
        player.gravity()

    ply.draw(scr)



    for plat in act_room.room_surfaces:
        for player in ply:
            if player.collided == True:
                plat.activate()

    pygame.display.flip()
    ticks.tick(60)
pygame.quit()
sys.exit()