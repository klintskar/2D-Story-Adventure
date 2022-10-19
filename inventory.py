import pygame
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.init()
FPS=15
fpsClock = pygame.time.Clock()
WIDTH, HEIGHT = WIN.get_size()
xpos=0
ypos=0
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

dagger=[2,"dagger", pygame.image.load("dagger.png"), "nonconsumable"]
sword=[5, "sword", pygame.image.load("sword.png"), "nonconsumable"]
axe=[4, "axe", pygame.image.load("axe.png"), "nonconsumable"]
pickaxe=[3, "pickaxe", pygame.image.load("pickaxe.png"), "nonconsumable"]
chainmail=[2, "chainmail", pygame.image.load("chainmail.png"),"nonconsumable"]
splint=[3, "splint", pygame.image.load("splint.png"),"nonconsumable"]
halfplatearmor=[4,"half plate armor",pygame.image.load("halfplatearmor.png"), "nonconsumable"]
platearmor=[5, "plate armor",pygame.image.load("platearmor.png"), "nonconsumable"]
elthezarsbomb=[6, "elthezars bomb",pygame.image.load("elthezarsbomb.png"),"consumable"]
healthpotion=[8, "health potion",pygame.image.load("healthpotion.png"), "consumable"]
orange=[2, "orange",pygame.image.load("orange.png"), "consumable"]
healthvial=[5,"health vial", pygame.image.load("healthvial.png"),"consumable"]
empty="empty"
#[position, value,name, image, consumable/nonconsumable, amount]
slot1=[position1,empty,empty,empty,empty,0]
slot2=[position2,empty,empty,empty,empty,0]
slot3=[position3,5,"health vial", pygame.image.load("healthvial.png"),"consumable",0]
slot4=[position4,empty,empty,empty,empty,0]
slot5=[position5,empty,empty,empty,empty,0]
slot6=[position6,empty,empty,empty,empty,0]
slot7=[position7,empty,empty,empty,empty,0]
slot8=[position8,empty,empty,empty,empty,0]
slot9=[position9,empty,empty,empty,empty,0]
slot10=[position10,empty,empty,empty,empty,0]
slot11=[position11,empty,empty,empty,empty,0]
slot12=[position12,empty,empty,empty,empty,0]

items=[slot1[1],slot2[1],slot3[1],slot4[1]]
itemposition=[slot1[0],slot2[0],slot3[0],slot4[0]]
inventorylist=[[slot1,slot2, slot3, slot4],
               [slot5,slot6,slot7,slot8],
               [slot9,slot10,slot11,slot12]]

#items:
WINWIDTH, WINHEIGHT = WIN.get_size()
inv=pygame.image.load("inventory.png")
inv= pygame. transform. scale(inv,(WIDTH,HEIGHT))

invstat=pygame.image.load("invstat.png")
invstat1=pygame.image.load("invstat.png")
invstat= pygame. transform. scale(invstat,((WIDTH/HEIGHT)*320,(WIDTH/HEIGHT)*385))
invstat1=pygame. transform. scale(invstat,((WIDTH/HEIGHT)*420,(WIDTH/HEIGHT)*154))
redbox=pygame.image.load("redbox.png")
redbox=pygame. transform. scale(redbox,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
boxposition=position1
def drawwindow(color):
    WIN.fill(color)
def inventory():
    clock=pygame.time.Clock()
    clock.tick(FPS)
    open=True
    while open:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                open=False
            drawinventory()
def drawslot():
    for y in range(3):
        for x in range(4):
            i=listinlist(listinlist(inventorylist,y),x)
            if i[3]!=empty:
                image=i[3]
                image=pygame.transform.scale(image,((WIDTH/HEIGHT)*70,(WIDTH/HEIGHT)*70))
                WIN.blit(image, i[0])
def drawinventory():
    i=listinlist(listinlist(inventorylist,ypos),xpos)
    WIN.blit(inv,(0,0))
    WIN.blit(invstat, (825,165))
    WIN.blit(invstat1, (80,570))
    WIN.blit(redbox,i[0])
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:#up
        move("up")
    if keys_pressed[pygame.K_RIGHT]:
        move("right")
    if keys_pressed[pygame.K_RIGHT]:
        move("down")
    if keys_pressed[pygame.K_RIGHT]:
        move("left")
    pygame.display.flip()
    drawslot()
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
    
def listinlist(list,index):
    return list[index]

def move(direction):
    global xpos
    global ypos
    if direction=="up":
        ypos=ypos-1
    if direction=="right":
        xpos=xpos+1
    if direction=="down":
        ypos=ypos+1
    if direction=="left":
        xpos=xpos-1
    
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

inventory()

