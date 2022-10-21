import pygame
from graphics import WINWIDTH
from graphics import WINHEIGHT

fade = pygame.image.load("fade.png")

wizardidle = [
            [0, 0, 86, 86, 8, (255, 255, 255)],
            [1, 0, 86, 86, 8, (255, 255, 255)],
            [2, 0, 86, 86, 8, (255, 255, 255)],
            [3, 0, 86, 86, 8, (255, 255, 255)],
            [4, 0, 86, 86, 8, (255, 255, 255)],
            [5, 0, 86, 86, 8, (255, 255, 255)],
            [4, 0, 86, 86, 8, (255, 255, 255)],
            [3, 0, 86, 86, 8, (255, 255, 255)],
            [2, 0, 86, 86, 8, (255, 255, 255)],
            [1, 0, 86, 86, 8, (255, 255, 255)],
            ]

wizardtext = ["I heard there is something tasty to the left","But I also heard that there is something valuable to the right","Beware of the dangers to come, now choose"]

heart = "heart.png"
blackheart = "blackheart.png"

# Alla object på våra maps och vart dom ligger plaserade
# Först bild, sen tuple med placering på bilden där 0.5 är mitten och 1 är längst bort
# Exempel:
#startroomobjects = ["wizardpath.png",(0,0.5)]


#forestfadetext = ["Detta är en skog. Skogibogitog","Oj ett träd","Shit en kebab!"]
startfadetext = []
##wizardfadetext = []
#combatfadetext = []

# Enemies:
#Picture, HP, DMG, Name, kill function number
swordskeleton1 = [pygame.image.load("swordskeleton.png"),15,2,"Sword wielding skeleton",1000]
swordskeleton2 = [pygame.image.load("swordskeleton.png"),15,2,"Sword wielding skeleton",2000]
ballskeleton = [pygame.image.load("ballskeleton.png"),15,4,"Spiked ball wielding skeleton",3000]
shieldskeleton1 = [pygame.image.load("shieldskeleton.png"),20,3,"Shield wielding skeleton",4000]
shieldskeleton2 = [pygame.image.load("shieldskeleton.png"),20,3,"Shield wielding skeleton",5000]

def kill(number):
        if number == 1000:
                room3[9] = "path"
        if number == 2000:
                room5[9] = "path"
        if number == 3000:
                room8[9] = "path"
        if number == 4000:
                room12[9] = "path"
        if number == 5000:
                room13[9] = "path"

# 0-Bild, Kan gå 1-Up, 2-höger, 3-ner, 4-vänster, 5,6,7,8-namn på hållen, 9-vilken typ av rum, 20-bild för fade in, 11-text för fade in,
# 12-object som ska printas på rummet (när rummet är path), 13-monstret om combat, 13-text till person om rummet är textbox,
# 14-idle bild för person i textbox, 15-idle lista med hur idle ser ut

room1fadetext = []
room1objects = []
room1 = [pygame.image.load("room1.png"),False,True,True,False,"","","","","path",pygame.image.load("room1.png"),room1fadetext,room1objects]

startroom = []

room2fadetext = []
room2objects = []
room2 = [pygame.image.load("room1.png"),False,True,True,True,"","","","","path",pygame.image.load("room1.png"),room2fadetext,room1objects]

room3fadetext = []
room3objects = []
room3 = [pygame.image.load("room1.png"),False,False,True,True,"","","","","combat",pygame.image.load("room1.png"),room3fadetext,room3objects,swordskeleton1]

room4fadetext = []
room4objects = []
room4 = [pygame.image.load("room1.png"),True,True,True,False,"","","","","path",pygame.image.load("room1.png"),room4fadetext,room4objects]

room5fadetext = []
room5objects = []
room5 = [pygame.image.load("room1.png"),True,True,True,True,"","","","","combat",pygame.image.load("room1.png"),room5fadetext,room5objects,swordskeleton2]

room6fadetext = []
room6objects = []
room6 = [pygame.image.load("room1.png"),True,False,True,True,"","","","","path",pygame.image.load("room1.png"),room6fadetext,room6objects]

room7fadetext = []
room7objects = []
room7 = [pygame.image.load("room1.png"),True,True,False,False,"","","","","path",pygame.image.load("room1.png"),room7fadetext,room7objects]

room8fadetext = []
room8objects = []
room8 = [pygame.image.load("room1.png"),True,True,True,True,"","","","","combat",pygame.image.load("room1.png"),room8fadetext,room8objects,ballskeleton]

room9fadetext = ["You met a very old wizard"]
room9 = [pygame.image.load("background1.png"),True,True,True,True,"","","","","textbox",pygame.image.load("background1.png"),room9fadetext,wizardtext,"idle.png",wizardidle]

healthroomfadetext = []
healthroomobjects = []
healthroom = [pygame.image.load("room1.png"),False,True,False,False,"","","","","path",pygame.image.load("room1.png"),healthroomfadetext,healthroomobjects]

weaponroomfadetext = []
weaponroomobjects = []
weaponroom = [pygame.image.load("room1.png"),False,False,False,True,"","","","","path",pygame.image.load("room1.png"),weaponroomfadetext,weaponroomobjects]

# Måste byta person man snackar med här, är wizard igen.
choicefadetext = []
choice = [pygame.image.load("background1.png"),True,True,True,True,"","","","","textbox",pygame.image.load("background1.png"),choicefadetext,wizardtext,"idle.png",wizardidle]
fight1 = []
fight2 = []

room10fadetext = []
room10objects = []
room10 = [pygame.image.load("room1.png"),False,True,True,False,"","","","","path",pygame.image.load("room1.png"),room10fadetext,room10objects]

room11fadetext = []
room11objects = []
room11 = [pygame.image.load("room1.png"),True,True,True,True,"","","","","path",pygame.image.load("room1.png"),room11fadetext,room11objects]

room12fadetext = []
room12objects = []
room12 = [pygame.image.load("room1.png"),False,False,True,True,"","","","","combat",pygame.image.load("room1.png"),room12fadetext,room12objects,shieldskeleton1]

room13fadetext = []
room13objects = []
room13 = [pygame.image.load("room1.png"),True,True,True,False,"","","","","combat",pygame.image.load("room1.png"),room13fadetext,room13objects,shieldskeleton1]

room14fadetext = []
room14objects = []
room14 = [pygame.image.load("room1.png"),True,True,True,True,"","","","","path",pygame.image.load("room1.png"),room14fadetext,room14objects]

room15fadetext = [] # Enter restroom text
room15objects = [] #Resting room objects
room15 = [pygame.image.load("room1.png"),True,False,True,True,"","","","","path",pygame.image.load("room1.png"),room15fadetext,room15objects]

room14 = []
room15 = []

room16fadetext = [""]
room16objects = []
room16 = [pygame.image.load("room16.png"),True,True,True,False,"","","","","path",pygame.image.load("room16.png"),room16fadetext,room16objects]
room17 = []
room18 = []
room19 = []
room20 = []
room21 = []
fakeroom = []
boss1 = []
boss2 = []
boss3 = []
boss4 = []

# Kartan
map = [fakeroom,[startroom],
      [fakeroom,room1,room2,room3],
      [fakeroom,room4,room5,room6],
      [fakeroom,room7,room8,room9],
  [healthroom,fight1,choice,fight2,weaponroom],
      [fakeroom,room10,room11,room12],
      [fakeroom,room13,room14,room15],
      [fakeroom,room16,room17,room18],
      [fakeroom,room19,boss1,room21],
      [fakeroom,fakeroom,boss2,fakeroom],
      [fakeroom,fakeroom,boss3,fakeroom],
      [fakeroom,fakeroom,boss4,fakeroom],]
mapcheckpoint = []

def save_checkpoint():
        global mapcheckpoint
        mapcheckpoint = list(map)
        global inventorylistcheckpoint
        inventorylistcheckpoint = list(inventorylist)

        global slot1copy
        global slot2copy
        global slot3copy
        global slot4copy
        global slot5copy
        global slot6copy
        global slot7copy
        global slot8copy
        global slot9copy
        global slot10copy
        global slot11copy
        global slot12copy
        for x in range(6):
                slot1copy[x] = slot1[x]
        for x in range(6):
                slot2copy[x] = slot2[x]
        for x in range(6):
                slot3copy[x] = slot3[x]
        for x in range(6):
                slot4copy[x] = slot4[x]
        for x in range(6):
                slot5copy[x] = slot5[x]
        for x in range(6):
                slot6copy[x] = slot6[x]
        for x in range(6):
                slot7copy[x] = slot7[x]
        for x in range(6):
                slot8copy[x] = slot8[x]
        for x in range(6):
                slot9copy[x] = slot9[x]
        for x in range(6):
                slot10copy[x] = slot10[x]
        for x in range(6):
                slot11copy[x] = slot11[x]
        for x in range(6):
                slot12copy[x] = slot12[x]

def load_checkpoint():
        global map
        global inventorylist
        map = list(mapcheckpoint)
        inventorylist = list(inventorylistcheckpoint)

        global slot1
        global slot2
        global slot3
        global slot4
        global slot5
        global slot6
        global slot7
        global slot8
        global slot9
        global slot10
        global slot11
        global slot12
        for x in range(6):
                slot1[x] = slot1copy[x]
        for x in range(6):
                slot2[x] = slot2copy[x]
        for x in range(6):
                slot3[x] = slot3copy[x]
        for x in range(6):
                slot4[x] = slot4copy[x]
        for x in range(6):
                slot5[x] = slot5copy[x]
        for x in range(6):
                slot6[x] = slot6copy[x]
        for x in range(6):
                slot7[x] = slot7copy[x]
        for x in range(6):
                slot8[x] = slot8copy[x]
        for x in range(6):
                slot9[x] = slot9copy[x]
        for x in range(6):
                slot10[x] = slot10copy[x]
        for x in range(6):
                slot11[x] = slot11copy[x]
        for x in range(6):
                slot12[x] = slot12copy[x]

########################################################################################

position1=(WINWIDTH*0.07,WINHEIGHT*0.19)
position2=(WINWIDTH*0.192,WINHEIGHT*0.19)
position3=(WINWIDTH*0.315,WINHEIGHT*0.19)
position4=(WINWIDTH*0.44,WINHEIGHT*0.19)

position5=(WINWIDTH*0.07,WINHEIGHT*0.35)
position6=(WINWIDTH*0.192,WINHEIGHT*0.35)
position7=(WINWIDTH*0.315,WINHEIGHT*0.35)
position8=(WINWIDTH*0.44,WINHEIGHT*0.35)

position9=(WINWIDTH*0.07,WINHEIGHT*0.51)
position10=(WINWIDTH*0.192,WINHEIGHT*0.51)
position11=(WINWIDTH*0.315,WINHEIGHT*0.51)
position12=(WINWIDTH*0.44,WINHEIGHT*0.51)

dagger=[2,"dagger", pygame.image.load("dagger.png"), "nonconsumable",1]
sword=[5, "sword", pygame.image.load("sword.png"), "nonconsumable",1]
axe=[4, "axe", pygame.image.load("axe.png"), "nonconsumable",1]
pickaxe=[3, "pickaxe", pygame.image.load("pickaxe.png"), "nonconsumable",1]
chainmail=[10, "chainmail", pygame.image.load("chainmail.png"),"nonconsumable",1]
splint=[20, "splint", pygame.image.load("splint.png"),"nonconsumable",1]
halfplatearmor=[30,"half plate armor",pygame.image.load("halfplatearmor.png"), "nonconsumable",1]
platearmor=[40, "plate armor",pygame.image.load("platearmor.png"), "nonconsumable",1]
elthezarsbomb=[6, "elthezars bomb",pygame.image.load("elthezarsbomb.png"),"consumable",1]
healthpotion=[8, "health potion",pygame.image.load("healthpotion.png"), "consumable",1]
orange=[2, "orange",pygame.image.load("orange.png"), "consumable",1]
healthvial=[5,"health vial", pygame.image.load("healthvial.png"),"consumable",1]
empty="empty"
#[position, value,name, image, consumable/nonconsumable, amount]
slot1=[position1,2,"dagger", pygame.image.load("dagger.png"), "nonconsumable",1]
slot2=[position2,10, "chainmail", pygame.image.load("chainmail.png"),"nonconsumable",1]
slot3=[position3,2, "orange",pygame.image.load("orange.png"), "consumable",2]
slot4=[position4,empty,empty,empty,empty,0]

slot5=[position5,empty,empty,empty,empty,0]
slot6=[position6,empty,empty,empty,empty,0]
slot7=[position7,empty,empty,empty,empty,0]
slot8=[position8,empty,empty,empty,empty,0]

slot9=[position9,empty,empty,empty,empty,0]
slot10=[position10,empty,empty,empty,empty,0]
slot11=[position11,empty,empty,empty,empty,0]
slot12=[position12,empty,empty,empty,empty,0]

slot1copy=[position1,empty,empty,empty,empty,0]
slot2copy=[position2,empty,empty,empty,empty,0]
slot3copy=[position3,empty,empty,empty,empty,0]
slot4copy=[position4,empty,empty,empty,empty,0]

slot5copy=[position5,empty,empty,empty,empty,0]
slot6copy=[position6,empty,empty,empty,empty,0]
slot7copy=[position7,empty,empty,empty,empty,0]
slot8copy=[position8,empty,empty,empty,empty,0]

slot9copy=[position9,empty,empty,empty,empty,0]
slot10copy=[position10,empty,empty,empty,empty,0]
slot11copy=[position11,empty,empty,empty,empty,0]
slot12copy=[position12,empty,empty,empty,empty,0]

def head(list):
       a = [""]
       a[0] = list[0]
       return a

def listinlist(list,index):
    return list[index]

def changeslot(invy,invx,change):
    global slot1
    global slot2
    global slot3
    global slot4
    global slot5
    global slot6
    global slot7
    global slot8
    global slot9
    global slot10
    global slot11
    global slot12
    if invy == 0 and invx == 0:
        for x in range(len(change)):
            slot1[x+1] = change[x]
    if invy == 0 and invx == 1:
        for x in range(len(change)):
            slot2[x+1] = change[x]
    if invy == 0 and invx == 2:
        for x in range(len(change)):
            slot3[x+1] = change[x]
    if invy == 0 and invx == 3:
         for x in range(len(change)):
            slot4[x+1] = change[x]
    if invy == 1 and invx == 0:
         for x in range(len(change)):
            slot5[x+1] = change[x]
    if invy == 1 and invx == 1:
         for x in range(len(change)):
            slot6[x+1] = change[x]
    if invy == 1 and invx == 2:
         for x in range(len(change)):
            slot7[x+1] = change[x]
    if invy == 1 and invx == 3:
         for x in range(len(change)):
            slot8[x+1] = change[x]
    if invy == 2 and invx == 0:
         for x in range(len(change)):
            slot9[x+1] = change[x]
    if invy == 2 and invx == 1:
         for x in range(len(change)):
            slot10[x+1] = change[x]
    if invy == 2 and invx == 2:
         for x in range(len(change)):
            slot11[x+1] = change[x]
    if invy == 2 and invx == 3:
         for x in range(len(change)):
            slot12[x+1] = change[x]

inventorylist = [[slot1,slot2, slot3, slot4],
                 [slot5,slot6,slot7,slot8],
                 [slot9,slot10,slot11,slot12]]
inventorylistcheckpoint = []

########################################################################################
