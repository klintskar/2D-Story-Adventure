import pygame
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()
FPS=15
fpsClock = pygame.time.Clock()
WIDTH, HEIGHT = WIN.get_size()

WHITE=(255,255,255)

position1=((WIDTH/HEIGHT)*60,(WIDTH/HEIGHT)*95)
position2=((WIDTH/HEIGHT)*165,(WIDTH/HEIGHT)*95)
position3=((WIDTH/HEIGHT)*275,(WIDTH/HEIGHT)*95)
position4=((WIDTH/HEIGHT)*380,(WIDTH/HEIGHT)*95)
position5=((WIDTH/HEIGHT)*60,(WIDTH/HEIGHT)*170)
position6=((WIDTH/HEIGHT)*165,(WIDTH/HEIGHT)*170)
position7=((WIDTH/HEIGHT)*275,(WIDTH/HEIGHT)*170)
position8=((WIDTH/HEIGHT)*380,(WIDTH/HEIGHT)*170)
position9=((WIDTH/HEIGHT)*60,(WIDTH/HEIGHT)*247)
position10=((WIDTH/HEIGHT)*165,(WIDTH/HEIGHT)*247)
position11=((WIDTH/HEIGHT)*275,(WIDTH/HEIGHT)*247)
position12=((WIDTH/HEIGHT)*380,(WIDTH/HEIGHT)*247)


pos1move=[position9,position2,position5,position4]
pos2move=[position10,position3,position6,position1]
pos3move=[position11,position4,position7,position2]
pos4move=[position12,position1,position8,position3]
pos5move=[position1,position6,position9,position8]
pos6move=[position2,position7,position10,position5]
pos7move=[position3,position8,position11,position6]
pos8move=[position4,position5,position12,position7]
pos9move=[position5,position10,position1,position12]
pos10move=[position6,position11,position2,position9]
pos11move=[position7,position12,position3,position10]
pos12move=[position8,position9,position4,position11]

rapier=[2,"dagger", "dagger.png", "nonconsumable"]
sword=[5, "sword", "sword.png", "nonconsumable"]
axe=[4, "axe", "axe.png", "nonconsumable"]
pickaxe=[3, "pickaxe", "pickaxe.png", "nonconsumable"]
chainmail=[2, "chainmail", "chainmail.png","nonconsumable"]
splint=[3, "splint", "splint.png","nonconsumable"]
halfplatearmor=[4,"half plate armor","halfplatearmor.png", "nonconsumable"]
platearmor=[5, "plate armor","platearmor.png", "nonconsumable"]
elthezarsbomb=[6, "elthezars bomb","elthezarsbomb.png","consumable"]
healthpotion=[8, "health potion","healthpotion.png", "consumable"]
orange=[2, "orange","orange.png", "consumable"]
healthvial=[5,"health vial", "healthvial.png","consumable"]
empty="empty"
#[position, name, image, consumable/nonconsumable, amount]
slot1=[position1,empty,empty,empty,0]
slot2=[position2,empty,empty,empty,0]
slot3=[position3,empty,empty,empty,0]
slot4=[position4,empty,empty,empty,0]
slot5=[position5,empty,empty,empty,0]
slot6=[position6,empty,empty,empty,0]
slot7=[position7,empty,empty,empty,0]
slot8=[position8,empty,empty,empty,0]
slot9=[position9,empty,empty,empty,0]
slot10=[position10,empty,empty,empty,0]
slot11=[position11,empty,empty,empty,0]
slot12=[position12,empty,empty,empty,0]

items=[slot1[1],slot2[1],slot3[1],slot4[1]]
itemposition=[slot1[0],slot2[0],slot3[0],slot4[0]]


#items:
WINWIDTH, WINHEIGHT = WIN.get_size()
inv=pygame.image.load("inventory.png")
inv= pygame. transform. scale(inv,(WIDTH,HEIGHT))
dagger=pygame.image.load("dagger.png")
dagger= pygame. transform. scale(dagger,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
sword=pygame.image.load("sword.png")
sword= pygame. transform. scale(sword,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
axe=pygame.image.load("axe.png")
axe= pygame. transform. scale(axe,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
pickaxe=pygame.image.load("pickaxe.png")
pickaxe= pygame. transform. scale(pickaxe,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
chainmail=pygame.image.load("chainmail.png")
chainmail= pygame. transform. scale(chainmail,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
splint=pygame.image.load("splint.png")
splint= pygame. transform. scale(splint,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
halfplatearmor=pygame.image.load("halfplatearmor.png")
halfplatearmor= pygame. transform. scale(halfplatearmor,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
platearmor=pygame.image.load("platearmor.png")
platearmor= pygame. transform. scale(platearmor,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
elthezarsbomb=pygame.image.load("elthezarsbomb.png")
elthezarsbomb= pygame. transform. scale(elthezarsbomb,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
healthvial=pygame.image.load("healthvial.png")
healthvial= pygame. transform. scale(healthvial,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
healthpotion=pygame.image.load("healthpotion.png")
healthpotion= pygame. transform. scale(healthpotion,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
orange=pygame.image.load("orange.png")
orange= pygame. transform. scale(orange,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
invstat=pygame.image.load("invstat.png")
invstat1=pygame.image.load("invstat.png")
invstat= pygame. transform. scale(invstat,((WIDTH/HEIGHT)*320,(WIDTH/HEIGHT)*385))
invstat1=pygame. transform. scale(invstat,((WIDTH/HEIGHT)*420,(WIDTH/HEIGHT)*154))
redbox=pygame.image.load("redbox.png")
redbox=pygame. transform. scale(redbox,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
boxposition=position1
def drawwindow(color):
    WIN.fill(color)
def inventory(pos):
    clock=pygame.time.Clock()
    clock.tick(FPS)
    open=True
    while open:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                open=False
            WIN.blit(inv,(0,0))
            WIN.blit(sword, (position9))
            WIN.blit(healthpotion, position10)
            WIN.blit(orange, position3)
            WIN.blit(invstat, (825,165))
            WIN.blit(invstat1, (80,570))
            WIN.blit(redbox,pos)
            pygame.display.flip()
            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_UP]:#up
                move(pos,"up")
            if keys_pressed[pygame.K_RIGHT]:
                move(pos,"right")
            if keys_pressed[pygame.K_RIGHT]:
                move(pos,"down")
            if keys_pressed[pygame.K_RIGHT]:
                move(pos,"left")
def store(slot,pickedupitem):
    slot[1]=pickedupitem[1]
    slot[2]=pickedupitem[2]
    slot[3]=pickedupitem[3]
def add(slot):
    slot[4]==slot[4]+1

def getitem(pickedupitem):
    x=1
    for n in items:
        if pickedupitem==n:
            print(n)
            if x==1:
                add(slot1)
            if x==2:
                add(slot2)
            if x==3:
                add(slot3)
            if x==4:
                add(slot4)
            if x==5:
                add(slot5)
            if x==6:
                add(slot6)
            if x==7:
                add(slot7)
            if x==8:
                add(slot8)
            if x==9:
                add(slot9)
            if x==10:
                add(slot10)
            if x==11:
                add(slot11)
            if x==12:
                add(slot12)
            break
        elif n=="empty":
            if x==1:
                store(slot1,pickedupitem)
                print(slot1)
            if x==2:
                store(slot2,pickedupitem)
            if x==3:
                store(slot3,pickedupitem)
            if x==4:
                store(slot4,pickedupitem)
            if x==5:
                store(slot5,pickedupitem)
            if x==6:
                store(slot6,pickedupitem)
            if x==7:
                store(slot7,pickedupitem)
            if x==8:
                store(slot8,pickedupitem)
            if x==9:
                store(slot9,pickedupitem)
            if x==10:
                store(slot10,pickedupitem)
            if x==11:
                store(slot11,pickedupitem)
            if x==12:
                store(slot12,pickedupitem)
    x=x+1

def move(pos,direction):
    if boxposition==position1:
        if direction=="up":
            boxposition==pos1move[0]
            inventory(pos1move[0])
        elif direction=="right":
            inventory(pos1move[1])
            boxposition==pos1move[1]
        elif direction=="down":
            inventory(pos1move[2])
            boxposition==pos1move[2]
        elif direction=="left":
            inventory(pos1move[3])
            boxposition==pos1move[3]
    if boxposition==position2:
        if direction=="up":
            inventory(pos2move[0])
            boxposition==pos2move[0]
        elif direction=="right":
            inventory(pos2move[1])
            boxposition==pos2move[1]
        elif direction=="down":
            inventory(pos2move[2])
            boxposition==pos2move[2]
        elif direction=="left":
            inventory(pos2move[3])
            boxposition==pos2move[3]
    if boxposition==position3:
        if direction=="up":
            inventory(pos3move[0])
            boxposition==pos3move[0]
        elif direction=="right":
            inventory(pos3move[1])
            boxposition==pos3move[1]
        elif direction=="down":
            inventory(pos3move[2])
            boxposition==pos3move[2]
        elif direction=="left":
            inventory(pos3move[3])
            boxposition==pos3move[3]
    if boxposition==position4:
        if direction=="up":
            inventory(pos4move[0])
            boxposition==pos4move[0]
        elif direction=="right":
            inventory(pos4move[1])
            boxposition==pos4move[1]
        elif direction=="down":
            inventory(pos4move[2])
            boxposition==pos4move[2]
        elif direction=="left":
            inventory(pos4move[3])
            boxposition==pos4move[3]
    if boxposition==position5:
        if direction=="up":
            inventory(pos5move[0])
            boxposition==pos5move[0]
        elif direction=="right":
            inventory(pos5move[1])
            boxposition==pos5move[1]
        elif direction=="down":
            inventory(pos5move[2])
            boxposition==pos5move[2]
        elif direction=="left":
            inventory(pos5move[3])
            boxposition==pos5move[3]
    if boxposition==position6:
        if direction=="up":
            inventory(pos6move[0])
            boxposition==pos6move[0]
        elif direction=="right":
            inventory(pos6move[1])
            boxposition==pos6move[1]
        elif direction=="down":
            inventory(pos6move[2])
            boxposition==pos6move[2]
        elif direction=="left":
            inventory(pos6move[3])
            boxposition==pos6move[3]
    if boxposition==position7:
        if direction=="up":
            inventory(pos7move[0])
            boxposition==pos7move[0]
        elif direction=="right":
            inventory(pos7move[1])
            boxposition==pos7move[1]
        elif direction=="down":
            inventory(pos7move[2])
            boxposition==pos7move[2]
        elif direction=="left":
            inventory(pos7move[3])
            boxposition==pos7move[3]
    if boxposition==position8:
        if direction=="up":
            inventory(pos8move[0])
            boxposition==pos8move[0]
        elif direction=="right":
            inventory(pos8move[1])
            boxposition==pos8move[1]
        elif direction=="down":
            inventory(pos8move[2])
            boxposition==pos8move[2]
        elif direction=="left":
            inventory(pos8move[3])
            boxposition==pos8move[3]
    if boxposition==position9:
        if direction=="up":
            inventory(pos9move[0])
            boxposition==pos9move[0]
        elif direction=="right":
            inventory(pos9move[1])
            boxposition==pos9move[1]
        elif direction=="down":
            inventory(pos9move[2])
            boxposition==pos9move[2]
        elif direction=="left":
            inventory(pos9move[3])
            boxposition==pos9move[3]
    if boxposition==position10:
        if direction=="up":
            inventory(pos10move[0])
            boxposition==pos10move[0]
        elif direction=="right":
            inventory(pos10move[1])
            boxposition==pos10move[1]
        elif direction=="down":
            inventory(pos10move[2])
            boxposition==pos10move[2]
        elif direction=="left":
            inventory(pos10move[3])
            boxposition==pos10move[3]
    if boxposition==position11:
        if direction=="up":
            inventory(pos11move[0])
            boxposition==pos11move[0]
        elif direction=="right":
            inventory(pos11move[1])
            boxposition==pos11move[1]
        elif direction=="down":
            inventory(pos11move[2])
            boxposition==pos11move[2]
        elif direction=="left":
            inventory(pos11move[3])
            boxposition==pos11move[3]
    if boxposition==position1:
        if direction=="up":
            inventory(pos12move[0])
            boxposition==pos12move[0]
        elif direction=="right":
            inventory(pos12move[1])
            boxposition==pos12move[1]
        elif direction=="down":
            inventory(pos12move[2])
            boxposition==pos12move[2]
        elif direction=="left":
            inventory(pos12move[3])
            boxposition==pos12move[3]
    
def remove(slot):
    slot[5]=slot[5]-1
    if slot[5]==0:
        slot[1]=empty
        slot[2]=empty
        slot[3]=empty
def removeconsume():
    x=1
    for n in itemposition:
        if n==boxposition:
            if x==1:
                remove(slot1)
            if x==2:
                remove(slot2)
            if x==3:
                remove(slot3)
            if x==4:
                remove(slot4)
            if x==5:
                remove(slot5)
            if x==6:
                remove(slot6)
            if x==7:
                remove(slot7)
            if x==8:
                remove(slot8)
            if x==9:
                remove(slot9)
            if x==10:
                remove(slot10)
            if x==11:
                remove(slot11)
            if x==12:
                remove(slot12)      
        x=x+1
print(WIDTH, HEIGHT)
inventory(boxposition)
