import pygame
import information
import spritesheet
import time
import random

########################################################################################
#WIN = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Game Project")
pygame.font.init()
########################################################################################
font = pygame.font.SysFont('Comic Sins MS', 30)
WINWIDTH, WINHEIGHT = WIN.get_size()
UGLYGREEN = (30, 50, 40)
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CHARACTERINDEX = 0
start = time.time()
keystart = time.time()
keys_pressed = None
textbox = []
textboxindex = 0
currentlocationx = 1
currentlocationy = 1
player = {"hp":10,"dmg":2,"armor":10}
yesno = ""
fadeyn = False
fadetext = True
fighttext = ["",""]
########################################################################################
# Spritesheets
spritesheetimage = None
sprite_sheet = None

########################################################################################
# Checkpoints

player_checkpoint = {}
currentlocationx_checkpoint = 0
currentlocationy_Checkpoint = 0

def save_checkpoint():
    information.save_checkpoint()
    global player_checkpoint
    player_checkpoint = player.copy()

    global currentlocationx_checkpoint
    global currentlocationy_Checkpoint
    currentlocationx_checkpoint = currentlocationx
    currentlocationy_Checkpoint = currentlocationy

def load_checkpoint():
    information.load_checkpoint()
    global player
    player = player_checkpoint.copy()

    global currentlocationx
    global currentlocationy
    currentlocationx = currentlocationx_checkpoint
    currentlocationy = currentlocationy_Checkpoint

########################################################################################
# Player displays

def player_hp():
    heart = pygame.image.load(information.heart).convert_alpha()
    heart_sprite = spritesheet.SpriteSheet(heart)
    heart = heart_sprite.get_image(0, 0, 778, 594, (1/10), (255, 255, 255))
    for x in range (int(player["hp"])):
        WIN.blit(heart, (5+((x)*80),5))

def player_inventory():
    my_font = pygame.font.SysFont('Comic Sans MS', int((WINWIDTH+WINHEIGHT)/100))
    HP = my_font.render("HP: " + str(player["hp"]), False, (0, 0, 0))
    DMG = my_font.render("DMG: " + str(player["dmg"]), False, (0, 0, 0))
    ARMOR = my_font.render("ARMOR: " + str(player["armor"]), False, (0, 0, 0))
    WIN.blit(HP, (WINWIDTH/2 + WINWIDTH/14, WINHEIGHT/4))
    WIN.blit(DMG, (WINWIDTH/2 + WINWIDTH/14, 2*(WINHEIGHT/4)))
    if player["dmg"] == 2:
        image = information.dagger[2]
        image=pygame.transform.scale(image,((WINWIDTH*0.085,WINHEIGHT*0.14)))
        WIN.blit(image, (WINWIDTH/2 + WINWIDTH/14,(WINWIDTH+WINHEIGHT)/50 + 2*(WINHEIGHT/4)))
    elif player["dmg"] == 3:
        image = information.pickaxe[2]
        image=pygame.transform.scale(image,((WINWIDTH*0.085,WINHEIGHT*0.14)))
        WIN.blit(image, (WINWIDTH/2 + WINWIDTH/14,(WINWIDTH+WINHEIGHT)/50 + 2*(WINHEIGHT/4)))
    elif player["dmg"] == 4:
        image = information.axe[2]
        image=pygame.transform.scale(image,((WINWIDTH*0.085,WINHEIGHT*0.14)))
        WIN.blit(image, (WINWIDTH/2 + WINWIDTH/14,(WINWIDTH+WINHEIGHT)/50 + 2*(WINHEIGHT/4)))
    elif player["dmg"] == 5:
        image = information.sword[2]
        image=pygame.transform.scale(image,((WINWIDTH*0.085,WINHEIGHT*0.14)))
        WIN.blit(image, (WINWIDTH/2 + WINWIDTH/14,(WINWIDTH+WINHEIGHT)/50 + 2*(WINHEIGHT/4)))

    WIN.blit(ARMOR, (WINWIDTH/2 + WINWIDTH/14, 3*(WINHEIGHT/4)))
    if player["armor"] == 10:
        image = information.chainmail[2]
        image=pygame.transform.scale(image,((WINWIDTH*0.085,WINHEIGHT*0.14)))
        WIN.blit(image, (WINWIDTH/2 + WINWIDTH/14,(WINWIDTH+WINHEIGHT)/50 + 3*(WINHEIGHT/4)))
    elif player["armor"] == 20:
        image = information.splint[2]
        image=pygame.transform.scale(image,((WINWIDTH*0.085,WINHEIGHT*0.14)))
        WIN.blit(image, (WINWIDTH/2 + WINWIDTH/14,(WINWIDTH+WINHEIGHT)/50 + 3*(WINHEIGHT/4)))
    elif player["armor"] == 30:
        image = information.halfplatearmor[2]
        image=pygame.transform.scale(image,((WINWIDTH*0.085,WINHEIGHT*0.14)))
        WIN.blit(image, (WINWIDTH/2 + WINWIDTH/14,(WINWIDTH+WINHEIGHT)/50 + 3*(WINHEIGHT/4)))
    elif player["armor"] == 40:
        image = information.platearmor[2]
        image=pygame.transform.scale(image,((WINWIDTH*0.085,WINHEIGHT*0.14)))
        WIN.blit(image, (WINWIDTH/2 + WINWIDTH/14,(WINWIDTH+WINHEIGHT)/50 + 3*(WINHEIGHT/4)))

########################################################################################
# Inventory code
eating = False
removing = False
inventory = False

xpos=0
ypos=0

inv=pygame.image.load("inventory.png")
inv= pygame. transform. scale(inv,(WINWIDTH,WINHEIGHT))

invstat=pygame.image.load("invstat.png")
invstat1=pygame.image.load("invstat.png")
invstat= pygame. transform. scale(invstat,(WINWIDTH*0.382,WINHEIGHT*0.79))
invstat1=pygame. transform. scale(invstat,(WINWIDTH*0.488,WINHEIGHT*0.32))
redbox=pygame.image.load("redbox.png")
redbox=pygame.transform.scale(redbox,((WINWIDTH*0.085,WINHEIGHT*0.14)))

def fake_drawinventory():
    i=listinlist(listinlist(information.inventorylist,ypos),xpos)
    WIN.blit(inv,(0,0))
    WIN.blit(invstat, ( WINWIDTH*0.538,WINHEIGHT*0.19))
    WIN.blit(invstat1,( WINWIDTH*0.05,WINHEIGHT*0.66))
    WIN.blit(redbox,i[0])
    drawslot()
    player_inventory()

def drawinventory():
    global inventory
    global keystart
    global yesno
    global removing
    global eating
    i=listinlist(listinlist(information.inventorylist,ypos),xpos)
    WIN.blit(inv,(0,0))
    WIN.blit(invstat, ( WINWIDTH*0.538,WINHEIGHT*0.19))
    WIN.blit(invstat1,( WINWIDTH*0.05,WINHEIGHT*0.66))
    WIN.blit(redbox,i[0])
    keynow = time.time()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP] and (keystart + 0.25) < (keynow):#up
        if ypos != 0:
            move("up")
            keystart = time.time()
    if keys_pressed[pygame.K_RIGHT] and (keystart + 0.25) < (keynow):
        if xpos != 3:
            move("right")
            keystart = time.time()
    if keys_pressed[pygame.K_DOWN] and (keystart + 0.25) < (keynow):
        if ypos != 2:
            move("down")
            keystart = time.time()
    if keys_pressed[pygame.K_LEFT] and (keystart + 0.25) < (keynow):
        if xpos != 0:
            move("left")
            keystart = time.time()
    if keys_pressed[pygame.K_r] and (keystart + 0.25) < (keynow):
        yesno = "waiting"
        removing = True
        keystart = time.time()
    if yesno and removing and(keystart + 0.25) < (keynow):
        remove()
        yesno = False
        removing = False
        keystart = time.time()
    if keys_pressed[pygame.K_i] and (keystart + 0.25) < (keynow):
        inventory = False
        keystart = time.time()
    if keys_pressed[pygame.K_c] and (keystart + 0.25) < (keynow):
        yesno = "waiting"
        eating = True
        keystart = time.time()
    if yesno and eating and(keystart + 0.25) < (keynow):
        consume()
        yesno = False
        eating = False
        keystart = time.time()
    if keys_pressed[pygame.K_e] and (keystart + 0.25) < (keynow):
        equip()
        keystart = time.time()
    if keys_pressed[pygame.K_g] and (keystart + 0.25) < (keynow):
        getitem(information.splint)
        keystart = time.time()
    if keys_pressed[pygame.K_t] and (keystart + 0.25) < (keynow):
        re_sort()
        keystart = time.time()

    drawslot()
    player_inventory()
    pygame.display.flip()

def consume():
    i=listinlist(listinlist(information.inventorylist,ypos),xpos)
    if i[4] == "consumable":
        player["hp"] = player["hp"] + i[1]
        if player["hp"] > 10:
            player["hp"] = 10
        remove()

def equip():
    i=listinlist(listinlist(information.inventorylist,ypos),xpos)
    if i[4] == "nonconsumable" and player["armor"] != i[1] and player["dmg"] != i[1]:
        if i[2] == "chainmail":
            player["armor"] = i[1]
        if i[2] == "splint":
            player["armor"] = i[1]
        if i[2] == "half plate armor":
            player["armor"] = i[1]
        if i[2] == "plate armor":
            player["armor"] = i[1]
        if i[2] == "dagger":
            player["dmg"] = i[1]
        if i[2] == "pickaxe":
            player["dmg"] = i[1]
        if i[2] == "axe":
            player["dmg"] = i[1]
        if i[2] == "sword":
            player["dmg"] = i[1]
    elif i[4] == "nonconsumable" and player["armor"] == i[1]:
        player["armor"] = 0
    elif i[4] == "nonconsumable" and player["dmg"] == i[1]:
        player["dmg"] = 1

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

def tail(list):
    b = []
    for x in range (len(list)):
        b.append(list[x])
    b.pop(0)
    return b

def remove():
    i=listinlist(listinlist(information.inventorylist,ypos),xpos)
    if i[4] == "nonconsumable" and player["armor"] == i[1]:
        player["armor"] = 0
    if i[4] == "nonconsumable" and player["dmg"] == i[1]:
        player["dmg"] = 1
    if i[1] == "empty":
        pass
    elif i[5] > 1:
        i[5] = i[5] - 1
        information.changeslot(ypos,xpos,tail(i))
    else:
        list = ["empty","empty","empty","empty",0]
        information.changeslot(ypos,xpos,list)
        re_sort()

def getitem(pickedupitem):
    global keystart
    keynow = time.time()
    for y in range (3):
        for x in range (4):
            i=listinlist(listinlist(information.inventorylist,y),x)
            if i[1] == "empty" and i[2] != pickedupitem[1] and (keystart + 0.25) < (keynow):
                keystart = time.time()
                information.changeslot(y,x,pickedupitem)
                return None
            elif i[2] == pickedupitem[1] and (keystart + 0.25) < (keynow):
                keystart = time.time()
                i[5] = i[5] + 1
                information.changeslot(y,x,tail(i))
                return None

def re_sort():
    for y in range (2,-1,-1):
        for x in range (3,-1,-1):
            i=listinlist(listinlist(information.inventorylist,y),x)
            if i[1] != "empty":
                copy = i.copy()
                sortremove(y,x)
                getitem(tail(copy))
                return None

def sortremove(y,x):
    i=listinlist(listinlist(information.inventorylist,y),x)
    list = ["empty","empty","empty","empty",0]
    information.changeslot(y,x,list)

def drawslot():
    for y in range(3):
        for x in range(4):
            i=listinlist(listinlist(information.inventorylist,y),x)
            if i[3]!="empty":
                image=i[3]
                image=pygame.transform.scale(image,((WINWIDTH*0.085,WINHEIGHT*0.14)))
                WIN.blit(image, i[0])
                my_font = pygame.font.SysFont('Comic Sans MS', 30)
                text_surface = my_font.render(str(i[5]), False, (0, 0, 0))
                WIN.blit(text_surface, i[0])
########################################################################################
        
# Combat
enemyhp = 0
firstcombat = True

def damage(attacked,dmg):
    if attacked == "player":
        global player
        if dmg > player["armor"]/10:
            player["hp"] = player["hp"] - (dmg - player["armor"]/10)
    else:
        global enemyhp
        enemyhp = (enemyhp - dmg)

def openinventory():
    global keystart
    keystart = time.time()
    global inventory
    inventory = True

def combat(enemy):
    global keynow
    global keystart
    keys_pressed = pygame.key.get_pressed()
    keynow = time.time()
    i = listinlist(listinlist(listinlist(information.map,currentlocationy),currentlocationx),13)
    global fighttext
    if keys_pressed[pygame.K_f] and (keystart + 0.25) < (keynow): # f for fight
        fighttext[0] = ""
        attack("player",i[2]) #enemy attack player
        attack(enemy,player["dmg"]) #player attacking enemy
        keystart = time.time()
        print("------------")

    elif keys_pressed[pygame.K_i] and (keystart + 0.25) < (keynow): # i for inventory
        openinventory()
        keystart = time.time()

    elif keys_pressed[pygame.K_r] and (keystart + 0.25) < (keynow): # r for run
        fighttext[0] ="No running! Enemy tries one last attack when you turned! "
        attack("player",1)
        keystart = time.time()
        
def attack(attacked,dmg):
    global fighttext
    i = listinlist(listinlist(listinlist(information.map,currentlocationy),currentlocationx),13)
    hitormiss=random.randint(1,3)
    if hitormiss<3 and attacked == "player":
        fighttext[0] = fighttext[0] + f"The {i[3]}'s attack missed! "
        damage(attacked,0)
    elif attacked == "player":
        fighttext[0] = fighttext[0] + f"The {i[3]}'s attack hit! "
        damage(attacked,dmg)
    elif hitormiss<3:
        fighttext[0] = fighttext[0] + "The player's attack missed!"
        print(f" {attacked} was missed")
        damage(attacked,0)
    else:
        fighttext[0] = fighttext[0] + "The player's attack hit!"
        print(f" {attacked} was hit")
        damage(attacked,dmg)
    
    
def playervictory(enemy):
    global firstcombat
    fighttext[0] = f"you defeated {enemy}"
    firstcombat = True
    i = listinlist(listinlist(listinlist(information.map,currentlocationy),currentlocationx),13)
    information.kill(i[4])
    normal_music()

def initiatecombat(enemy):
    global fighttext
    global firstcombat
    if enemyhp>0 and player["hp"]>0:
        combat(enemy)
    elif enemyhp<1:
        playervictory(enemy)
    elif player["hp"]<1:
        firstcombat = True
        load_checkpoint()
        normal_music()
        
def draw_combat():
    draw_background()
    player_hp()
    enemy_hp()
    load_enemy()
    global textboxindex
    global fighttext
    global enemyhp
    global firstcombat
    i = listinlist(listinlist(listinlist(information.map,currentlocationy),currentlocationx),13)
    if firstcombat:
        battle_music()
        enemyhp = i[1]
        firstcombat = False
    initiatecombat(i[3])
    combat_next_text()
    draw_textbox(fighttext[textboxindex])
    pygame.display.update()

def combat_next_text():
    global keystart
    keys_pressed = pygame.key.get_pressed()
    keynow = time.time()
    if keys_pressed[pygame.K_TAB] and (keystart + 0.25) < (keynow):
        combat_update_text()
        keystart = time.time()
def combat_update_text():
    global textboxindex
    global combattext
    if textboxindex != 0:
        if textboxindex == (len(textbox)-1):
            fighttext[0] = ""
            textboxindex = 0
    else:
        textboxindex = 0

def enemy_hp():
    heart = pygame.image.load("blackheart.png").convert_alpha()
    heart_sprite = spritesheet.SpriteSheet(heart)
    heart = heart_sprite.get_image(0, 0, 862, 778, (1/10), (255, 255, 255))
    for x in range (enemyhp):
        WIN.blit(heart, (5+((x)*100),(WINHEIGHT - (WINHEIGHT/6)) - 80))

def load_enemy():
    i = listinlist(listinlist(listinlist(information.map,currentlocationy),currentlocationx),13)
    enemy = i[0]
    enemy = pygame.transform.scale(enemy, (WINWIDTH/3, WINHEIGHT/3))
    WIN.blit(enemy, (WINWIDTH*0.3 , WINHEIGHT*0.4))

########################################################################################
# Commonly used window functions

def yesnofunction():
    global yesno
    i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
    a = i[9]
    if inventory:
        fake_drawinventory()
    elif a == "textbox":
        fake_draw_text_window()
    elif a == "path":
        fake_draw_choose_path()

    picture = WIN.copy()
    font = pygame.font.SysFont('Comic Sans MS', int(WINHEIGHT/20))

    WIN.blit(picture, (0,0))
    middlex = WINWIDTH/2
    middley = WINHEIGHT/2
    pygame.draw.rect(WIN, WHITE, pygame.Rect( (middlex)-(WINWIDTH/16), (middley)-(WINHEIGHT/32), WINWIDTH/8, WINHEIGHT/16 ))
    pygame.draw.rect(WIN, BLACK, pygame.Rect( (middlex)-(WINWIDTH/16)+5, (middley)-(WINHEIGHT/32)+5, WINWIDTH/8 -10, WINHEIGHT/16 -10 ))
    blit_text(WIN, "Y or N", ((middlex)-(WINWIDTH/24), (middley)-(WINHEIGHT/30)), font)
    pygame.display.update()
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[pygame.K_y]:
        yesno = True
    elif keys_pressed[pygame.K_n]:
        yesno = False
    else:
        yesno = "waiting"

def draw_background():
    i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
    background = i[0]
    background = pygame.transform.scale(background, (WINWIDTH, WINHEIGHT))
    WIN.blit(background, (0, 0))

# Updates sprites for an animation effect
def update_animate(spritelist):
    global start
    global CHARACTERINDEX
    now = time.time()
    if now >= (start+(1/8)):
        if CHARACTERINDEX >= (len(spritelist)-1):
            CHARACTERINDEX = 0
        else:
            CHARACTERINDEX += 1
        start = now

# Function to return specific list in a list of lists (needed for other function to work)
def listinlist(list,index):
    return list[index]

# Function to switch map location
def location_switch():
    global textboxindex
    global keystart
    global currentlocationx
    global currentlocationy
    keys_pressed = pygame.key.get_pressed()
    keynow = time.time()
    i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
    if keys_pressed[pygame.K_UP] and (keystart + 0.25) < (keynow):
        if i[1]:
            currentlocationy -= 1
            fade_function()
            textboxindex = 0
        keystart = time.time()
    elif keys_pressed[pygame.K_RIGHT] and (keystart + 0.25) < (keynow):
        if i[2]:
            currentlocationx += 1
            fade_function()
            textboxindex = 0
        keystart = time.time()
    elif keys_pressed[pygame.K_DOWN] and (keystart + 0.25) < (keynow):
        if i[3]:
            currentlocationy += 1
            fade_function()
            textboxindex = 0
        keystart = time.time()
    elif keys_pressed[pygame.K_LEFT] and (keystart + 0.25) < (keynow):
        if i[4]:
            currentlocationx -= 1
            fade_function()
            textboxindex = 0
        keystart = time.time()

def update_spritesheet():
    global spritesheetimage
    global sprite_sheet
    i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
    spritesheetimage = pygame.image.load(i[13]).convert_alpha()
    sprite_sheet = spritesheet.SpriteSheet(spritesheetimage)

########################################################################################
# Specific draw textbox window functions

# Main function for textbox window
def draw_text_window():
    global textbox
    i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
    textbox = listinlist(i,12)
    update_spritesheet()
    next_text()
    draw_background()
    update_animate(listinlist(i,14))
    draw_character(sprite_sheet, listinlist(i,14))
    draw_textbox(textbox[textboxindex])
    location_switch()
    pygame.display.update()

# Fake version for fade (runs smoother)
def fake_draw_text_window():
    global textbox
    i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
    textbox = listinlist(i,12)
    update_spritesheet()
    draw_background()
    draw_character(sprite_sheet, listinlist(i,14))
    draw_textbox(textbox[textboxindex])

def draw_textbox(text):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    pygame.draw.rect(WIN, WHITE, pygame.Rect(0, (WINHEIGHT - (WINHEIGHT/6)), WINWIDTH, (WINHEIGHT/6)))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(10, ((WINHEIGHT - (WINHEIGHT/6))+10), (WINWIDTH-20), ((WINHEIGHT/6)-20)))
    blit_text(WIN, text, (10, ((WINHEIGHT - (WINHEIGHT/6))+6)), font)

def draw_character(spritesheet, spritelist):
    WINWIDTH, WINHEIGHT = WIN.get_size()
    for x in range(6):
        if x == 0:
            a = listinlist(spritelist,CHARACTERINDEX)[x]
        elif x == 1:
            b = listinlist(spritelist,CHARACTERINDEX)[x]
        elif x == 2:
            c = listinlist(spritelist,CHARACTERINDEX)[x]
        elif x == 3:
            d = listinlist(spritelist,CHARACTERINDEX)[x]
        elif x == 4:
            e = listinlist(spritelist,CHARACTERINDEX)[x]
        elif x == 5:
            f = listinlist(spritelist,CHARACTERINDEX)[x]

    character = spritesheet.get_image(a,b,c,d,e,f)
    WIN.blit(character, ((WINWIDTH - character.get_width()), WINHEIGHT - character.get_height()))

# Places text on screen inside the textbox
def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width: # Checks if the next word added to the line is inside the textbox
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

# These 2 functions updates the text shown in the textbox
def next_text():
    global keystart
    keys_pressed = pygame.key.get_pressed()
    keynow = time.time()
    if keys_pressed[pygame.K_TAB] and (keystart + 0.25) < (keynow):
        update_text()
        keystart = time.time()
def update_text():
    global textboxindex
    if textboxindex != 0:
        if textboxindex == (len(textbox)-1):
            textboxindex = 0
        else:
            textboxindex += 1
    else:
        textboxindex += 1

########################################################################################

def draw_choose_path():
    global keystart
    keynow = time.time()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_i] and (keystart + 0.25) < (keynow): # i for inventory
        openinventory()
        keystart = time.time()
    draw_background()
    player_hp()
    path_objects()
    location_switch()
    pygame.display.update()

# Fake version for fade (runs smoother)
def fake_draw_choose_path():
    draw_background()
    player_hp()
    path_objects()

# Ritar alla object vi har plaserat på bakgrunden
def path_objects():
    i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
    if not listinlist(i,12):
        pass
    else:
        for x in range(len(listinlist(i,12))):
            if x%2 == 0:
                a = listinlist(i,12)
                object = pygame.image.load(a[x]).convert_alpha()
                object_sprite = spritesheet.SpriteSheet(object)
                object = object_sprite.get_image(0, 0, 208, 288, 1, (255, 255, 255))
                tuple = listinlist(a,x+1)
                WIN.blit(object, (tuple[0]*WINWIDTH, tuple[1]*WINHEIGHT-32))

########################################################################################

# Fadar in en bild på skärmen och sedan fadar ut den samtidigt som scenen byts
def fade_function():
    global textboxindex
    textboxindex = 0
    global fadeyn
    global fadetext
    fadetext = True
    fadeyn = True
    fade_in_screen()

def fade_in_screen():
    i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
    fade = i[10]
    fade = pygame.transform.scale(fade, (WINWIDTH, WINHEIGHT))
    first = time.time()
    x = 0
    while x <= 100:
        now = time.time()
        if (now) >= (first + 0.1):
            first = now
            x = x + 20
            fade.set_alpha(x)
            WIN.blit(fade, (0, 0))
            pygame.display.update()

def fade_waiting():
    draw_fade_background()
    fade_next_text
    fade_text()
    pygame.display.update()


def fade_text():
    global textbox
    global fadeyn
    i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
    textbox = listinlist(i,11)
    if not listinlist(i,11):
        fadeyn = False
        fade_out_screen()
    else:
        if fade_next_text():
            draw_textbox(textbox[textboxindex])
        else:
            fadeyn = False
            fade_out_screen()

def fade_next_text():
    global keystart
    keys_pressed = pygame.key.get_pressed()
    keynow = time.time()
    if keys_pressed[pygame.K_TAB] and (keystart + 0.25) < (keynow):
        fade_update_text()
        keystart = time.time()
    if fadetext:
        return True
    else:
        return False

def fade_update_text():
    global textboxindex
    global fadetext
    if textboxindex != 0:
        if textboxindex == (len(textbox)-1):
            fadetext = False
            textboxindex = 0
        else:
            textboxindex += 1
    else:
        if (textboxindex+1) > (len(textbox)-1):
                fadetext = False
                textboxindex = 0
        else:
            textboxindex += 1



def draw_fade_background():
    i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
    background = i[10]
    background = pygame.transform.scale(background, (WINWIDTH, WINHEIGHT))
    WIN.blit(background, (0, 0))

def fade_out_screen():
    i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
    fade = i[10]
    fade = pygame.transform.scale(fade, (WINWIDTH, WINHEIGHT))
    x = 400
    first = time.time()
    a = i[9]
    if a == "textbox":
        fake_draw_text_window()
    if a == "path":
        fake_draw_choose_path()  
    picture = WIN.copy()
    while x > 0:
        now = time.time()
        if now >= (first + 0.1):
            WIN.blit(picture, (0, 0))
            fade.set_alpha(x)
            WIN.blit(fade, (0, 0))
            pygame.display.update()
            x = x - 40
            first = now

########################################################################################

def normal_music():
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("game_music.wav")
    pygame.mixer.music.play(-1)
    
def battle_music():
    pygame.mixer.init()
    pygame.mixer.music.stop()
    pygame.mixer.music.load("battle_music.wav")
    pygame.mixer.music.play(-1)

########################################################################################

# Pygame start function

def graphics():
    normal_music()

    clock = pygame.time.Clock()
    run = True
    global key_pressed
    save_checkpoint()
    
    while run:
        
        global yesno

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_ESCAPE]:
            pygame.quit()
        elif keys_pressed[pygame.K_w]:
            yesno = "waiting"
        elif keys_pressed[pygame.K_s]:
            pass
        
        i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)

        if yesno == "waiting":
            yesnofunction()
        elif fadeyn:
            fade_waiting()
        elif inventory:
            drawinventory()
        elif i[9] == "textbox":
            draw_text_window()
        elif i[9] == "path":
            draw_choose_path()
        elif i[9] == "combat":
            draw_combat()
    
    pygame.quit()

#This stops main from running if this file is imported
if __name__ == "__main__":
    graphics()
