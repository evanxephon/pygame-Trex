import pygame as pg
import time as tm
import math as mh
import random as rd
from sys import exit
from pygame.locals import *

sprite_image_filename = 'spirit1.png'
spriteDefinition = {
    'CACTUS_LARGE': {'x': 652, 'y': 2},
    'CACTUS_SMALL': {'x': 446, 'y': 2},
    'CLOUD': {'x': 166, 'y': 2},
    'HORIZON': {'x': 2, 'y': 104},
    'MOON': {'x': 954, 'y': 2},
    'PTERODACTYL': {'x': 260, 'y': 2},
    'RESTART': {'x': 2, 'y': 2},
    'TEXT_SPRITE': {'x': 1294, 'y': 2},
    'TREX': {'x': 1678, 'y': 2},
    'STAR': {'x': 1276, 'y': 2}
}
pg.init()
screen = pg.display.set_mode((1200,300),0,32)
sprite = pg.image.load(r'C:\Users\evanxephon\Desktop\Trex\%s'%(sprite_image_filename)).convert()


class Background:
    collide =[]
    s = ['LARGE','SMALL']
    size = rd.sample(s,1)
    bg_color = [255, 255, 255]
    time = tm.localtime(tm.time())
    star = []
    planet = []
    ground = []
    small_cactus = []
    large_cactus = []

    def dayornight(self):
        if not 6 < self.time.tm_hour < 18:
            self.bg_color = [0,0,0]
            return False
        else:
            return True

    def drawground(self):
        self.ground = []
        self.ground.append(rd.randint(0,1220))
        self.ground.append(rd.randint(0,1220))
        screen.blit(sprite,(0,248),(self.ground[0],spriteDefinition['HORIZON']['y'],1220,52))
        screen.blit(sprite,(1220,248),(self.ground[1],spriteDefinition['HORIZON']['y'],1220,52))

    def keepground(self):

        screen.blit(sprite,(0,248),(self.ground[0],spriteDefinition['HORIZON']['y'],1220,52))
        screen.blit(sprite,(1220,248),(self.ground[1],spriteDefinition['HORIZON']['y'],1220,52))

    def drawcactus(self):
        self.large_cactus =[]
        self.small_cactus =[]
        increment = 200
        i1 = i2 =0
        for i in range(2):
            if 'SMALL'in self.size:
                self.small_cactus.append([rd.randint(increment%1200,increment%1200+400),rd.randint(200,230)])
                screen.blit(sprite,self.small_cactus[i1],(spriteDefinition['CACTUS_SMALL']['x'],spriteDefinition['CACTUS_SMALL']['y'],34,70))
                i1 += 1
                self.size = rd.sample(self.s,1)
                increment += rd.randint(500,700)
            elif 'LARGE'in self.size:
                self.large_cactus.append([rd.randint(increment%1200,increment%1200+400),rd.randint(200,210)])
                screen.blit(sprite,self.large_cactus[i2],(spriteDefinition['CACTUS_LARGE']['x'],spriteDefinition['CACTUS_LARGE']['y'],50,140))
                i2 += 1
                self.size = rd.sample(self.s,1)
                increment += rd.randint(500,700)

    def keepcactus(self):

        for cactus in self.small_cactus:
            screen.blit(sprite,cactus,(spriteDefinition['CACTUS_SMALL']['x'],spriteDefinition['CACTUS_SMALL']['y'],34,70))

        for cactus in self.large_cactus:
            screen.blit(sprite,cactus,(spriteDefinition['CACTUS_LARGE']['x'],spriteDefinition['CACTUS_LARGE']['y'],50,140))

    def keepstar(self):

        for k in self.star:
            screen.blit(sprite,k,(spriteDefinition['STAR']['x']-6,spriteDefinition['STAR']['y'],24,18))

    def drawplanet(self):
        self.planet = []
        if self.dayornight():
            self.planet = [rd.randint(1, 1140), 10]
            screen.blit(sprite,self.planet, (spriteDefinition['MOON']['x'] +120, spriteDefinition['MOON']['y'], 80, 80))
        else:
            self.planet = [rd.randint(1, 1140), 10]
            screen.blit(sprite,self.planet, (spriteDefinition['MOON']['x'], spriteDefinition['MOON']['y'], 40,80))

    def keepplanet(self):

        if self.dayornight():
            screen.blit(sprite,self.planet, (spriteDefinition['MOON']['x']+120,  spriteDefinition['MOON']['y'], 80, 80))
        else:
            screen.blit(sprite,self.planet, (spriteDefinition['MOON']['x'],  spriteDefinition['MOON']['y'], 40,80))

    def drawstar(self):
        self.star = []
        if self.dayornight() is False:
            a = rd.randint(2,4)
            for i in range(a):
                self.star.append([rd.randint(1,1200),rd.randint(20,140)])
            for k in self.star:
                screen.blit(sprite,k,(spriteDefinition['STAR']['x']-6,spriteDefinition['STAR']['y'],24,18))
                
    def collidebox(self):

        self.collide = []
        for cactus in self.small_cactus:
            cactus.append(34)
            cactus.append(70)
            self.collide.append(cactus)

        for cactus in self.large_cactus:
            cactus.append(50)     
            cactus.append(140)
            self.collide.append(cactus)


class Movething:

    def __init__(self):
        pass

    def draw(self):
        pass


class Trex(Movething):

    x = spriteDefinition['TREX']['x']
    y = spriteDefinition['TREX']['y']
    speed = 8
    position = []
    y_position0 = 0
    signal = 0
    sprite_pos = [x,y,88,92]
    sprite_pos1 = [2321,38,120,60]
    y_pos = []
    y_incre = 0
    signal0 = 0
    signal1 = 0

    def draw(self):
            self.sprite_pos = [self.x,self.y,88,92]
            self.y_incre = 0
            self.signal = 0
            self.y_pos = []
            self.position = []
            self.position = [10,rd.randint(190,200)]
            self.y_pos.append(self.position[1])
            self.y_position0 = self.position[1]
            y_position = self.position[1]
            for i in range(11):
                y_position -= 15
                self.y_pos.append(y_position)
            for j in range(10):
                y_position += 15
                self.y_pos.append(y_position)
            self.y_pos.append(self.y_position0)

            screen.blit(sprite,self.position,(self.x,self.y,88,92))

    def move(self):

        for event in pg.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                        if self.position[1] == self.y_position0:
                            self.y_incre = -10
                            self.signal = 0

                elif event.key == K_DOWN:
                    if self.position[1] < self.y_position0:
                        if 2 < self.signal < 12:
                            self.signal = 19 - self.signal + 4
                            if self.signal > 22:
                                self.signal = 18
                        if 12 <= self.signal < 20:
                            self.signal += 4
                            if self.signal > 22:
                                self.signal = 22

                    elif self.position[1] >= self.y_position0:
                        self.position[1] += 32

            if event.type == KEYUP:
                if event.key == K_DOWN:
                    if self.position[1] > self.y_position0:
                        if self.sprite_pos1 == [2321,38,120,60] or  self.sprite_pos1 == [2201,38,120,60]:
                            self.position[1] -= 32

        if self.signal0 == 1:
            self.sprite_pos[0] = 1942
            self.sprite_pos1 = [2201,38,120,60]
            self.signal0 = 0
        elif self.signal0 == 0:
            self.sprite_pos[0] = 1854
            self.sprite_pos1 = [2321,38,120,60]
            self.signal0 = 1

        self.position[0] += self.speed
        if self.y_incre == -10:
            if self.signal <= 22:
                self.signal += 1
                self.position[1] = self.y_pos[self.signal-1]
            else:
                self.y_incre = 0

        if self.position[1] > self.y_position0:
            screen.blit(sprite,self.position,self.sprite_pos1)
        elif self.position[1] <= self.y_position0:
            screen.blit(sprite,self.position,self.sprite_pos)

    def collide(self):
        for cactus in x.collide:
            if self.position[1] == self.y_position0:
                if cactus[2] == 34:
                    if (cactus[0]+2 < self.position[0] < (cactus[0]+32)) or (cactus[0]+3 < (self.position[0]+88) < cactus[0]+32):
                        if self.position[1]+84 > cactus[1] and  mh.sqrt(((cactus[0]+34-self.position[0])/2)**2+((cactus[1]+70-self.position[1])/2)**2) < 90:
                            return True
                if cactus[2] == 50:
                    if (cactus[0]+4 < self.position[0] < (cactus[0]+46)) or (cactus[0]+4<(self.position[0]+88) < cactus[0]+46):
                        if self.position[1]+84 > cactus[1] and  mh.sqrt(((cactus[0]+50-self.position[0])/2)**2+((cactus[1]+140-self.position[1])/2)**2) < 105:
                            return True

            elif self.position[1] > self.y_position0:
                if cactus[2] == 34:
                    if (cactus[0]+2 < self.position[0] < (cactus[0]+32)) or (cactus[0]+3 < (self.position[0]+120) < cactus[0]+32):
                        if self.position[1]+54 > cactus[1] and  mh.sqrt(((cactus[0]+34-self.position[0])/2)**2+((cactus[1]+70-self.position[1])/2)**2) < 90:
                            return True
                if cactus[2] == 50:
                    if (cactus[0]+4 < self.position[0] < (cactus[0]+46)) or (cactus[0]+4<(self.position[0]+120) < cactus[0]+46):
                        if self.position[1]+54 > cactus[1] and  mh.sqrt(((cactus[0]+50-self.position[0])/2)**2+((cactus[1]+140-self.position[1])/2)**2) < 105:
                            return True

    def win(self):
        if self.position[0] > 1200:
            screen.blit(sprite,(410,90),(1296,24,382,40))
            screen.blit(sprite,[561,120],[0,0,76,74])

            for event in pg.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    pressed_mouse = pg.mouse.get_pressed()
                    if pressed_mouse[0]:
                        pos = pg.mouse.get_pos()
                        if 561 < pos[0] < 639 and 111 < pos[1] < 185:
                            init()
                            play()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        init()
                        play()


class Cloud(Movething):
    
    speed = 0.2
    clouds = []
    a = rd.randint(2, 3)
    x = spriteDefinition['CLOUD']['x']
    y = spriteDefinition['CLOUD']['y']

    def draw(self):
        self.clouds = []
        for i in range(self.a):
            self.clouds.append([rd.randint(1,1150),rd.randint(2,150)])
        for k in self.clouds:
            screen.blit(sprite,k,(self.x,self.y,92,28))

    def move(self):
        for k in self.clouds:
            k[0] += self.speed
            k[0] = k[0] % 1200
            screen.blit(sprite,k,(self.x,self.y,92,28))


class Pterodactyl(Movething):
    speed = 4
    birds = []
    x = spriteDefinition['PTERODACTYL']['x']
    y = spriteDefinition['PTERODACTYL']['y']
    birdsprite = sprite.subsurface(x,y,92,95).copy()
    birdsprite = pg.transform.flip(birdsprite,True,False)

    def draw(self):
        self.birds = []
        a = rd.randint(1,2)
        b = 0
        for i in range(a):
            self.birds.append([rd.randint(800,1200),b,rd.choice([-1,1])])
            b += 150

        for bird in self.birds:
            screen.blit(sprite,bird[0:2],(self.x,self.y,92,95))

    def fly(self):

        for bird in self.birds:
            bird[0] += bird[2]*self.speed
            if not bird[0] > 1200 or bird[0] < 0:
                if bird[2] == 1:

                    screen.blit(self.birdsprite,bird[0:2])
                elif bird[2] == -1:

                    screen.blit(sprite,bird[0:2],(self.x,self.y,92,95))

    def collide(self):

        for bird in self.birds:
            if trex.position[1] <= trex.y_position0:
                    if (bird[0]+10 < trex.position[0] < (bird[0]+70)) or (bird[0]+10 < (trex.position[0]+88) < bird[0]+70):
                        if trex.position[1] < bird[1] + 70 and mh.sqrt(((bird[0]+92-trex.position[0])/2)**2+((bird[1]+95-trex.position[1])/2)**2) < 80:
                            return True
            if trex.position[1] > trex.y_position0:
                    if (bird[0]+10 < trex.position[0] < (bird[0]+70)) or (bird[0]+10 < (trex.position[0]+88) < bird[0]+70):
                        if trex.position[1] < bird[1] + 70 and mh.sqrt(((bird[0]+92-trex.position[0])/2)**2+((bird[1]+95-trex.position[1])/2)**2) < 80:
                            return True


x = Background()
bird = Pterodactyl()
trex = Trex()
cloud = Cloud()
x.dayornight()


def init():
    screen.fill(x.bg_color)
    trex.draw()
    cloud.draw()
    bird.draw()
    x.drawcactus()
    x.drawground()
    x.drawstar()
    x.drawplanet()
    x.collidebox()


def play():
    while not (trex.collide()or bird.collide()):
        screen.fill(x.bg_color,[0,0,1200,300])
        x.keepstar()
        x.keepplanet()
        x.keepground()
        x.keepcactus()
        cloud.move()
        bird.fly()
        trex.move()
        clock = pg.time.Clock()
        clock.tick(50)
        trex.win()
        pg.display.update([0,0,1200,300])
    if trex.collide()or bird.collide():
        screen.blit(sprite,[561,120],[0,0,76,74])
        pg.display.update([561,120,76,74])

init()
play()

while True:
    for event in pg.event.get():
        if event.type == MOUSEBUTTONDOWN:
            pressed_mouse = pg.mouse.get_pressed()
            if pressed_mouse[0]:
                pos = pg.mouse.get_pos()
                if 561 < pos[0] < 639 and 111 < pos[1] < 185:
                    init()
                    play()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                init()
                play()