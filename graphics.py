from cgitb import text
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
font = pygame.font.SysFont('Comic Sans MS', 30)
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
player ={"hp":10,"dmg":4}
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
currentlocationx_checkpoint = 1
currentlocationy_Checkpoint = 1

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
    for x in range (player["hp"]):
        WIN.blit(heart, (5+((x)*80),5))

########################################################################################
# Combat
enemyhp = 0
firstcombat = True

def damage(attacked,dmg):
    if attacked == "player":
        global player
        player["hp"] = player["hp"] - dmg
        print(player["hp"])
    else:
        global enemyhp
        enemyhp = (enemyhp - dmg)
        print(enemyhp)

def openinventory():
    pass

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
        
def draw_combat():
    draw_fade_background()
    player_hp()
    enemy_hp()
    load_enemy()
    global textboxindex
    global fighttext
    global enemyhp
    global firstcombat
    i = listinlist(listinlist(listinlist(information.map,currentlocationy),currentlocationx),13)
    if firstcombat:
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
        textboxindex += 1

def enemy_hp():
    heart = pygame.image.load(information.heart).convert_alpha()
    heart_sprite = spritesheet.SpriteSheet(heart)
    heart = heart_sprite.get_image(0, 0, 778, 594, (1/10), (255, 255, 255))
    for x in range (enemyhp):
        WIN.blit(heart, (5+((x)*80),(WINHEIGHT - (WINHEIGHT/6)) - 60))

def load_enemy():
    i = listinlist(listinlist(listinlist(information.map,currentlocationy),currentlocationx),13)
    enemy = i[0]
    enemy = pygame.transform.scale(enemy, (WINWIDTH/5, WINHEIGHT/6))
    WIN.blit(enemy, (WINWIDTH/2 -(WINWIDTH/10), WINHEIGHT/2 -(WINHEIGHT/12)))

########################################################################################
# Commonly used window functions

def yesnofunction():

    global yesno
    i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
    a = i[9]
    if a == "textbox":
        fake_draw_text_window()
    if a == "path":
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
        yesno = False
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
            x = textboxindex
            textboxindex = 0
        else:
            x = textboxindex
            textboxindex += 1
    else:
        x = textboxindex
        textboxindex += 1

########################################################################################

def draw_choose_path():
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

# Pygame start function

def graphics():
    
    pygame.mixer.init()
    pygame.mixer.music.load("game_music.wav")
    pygame.mixer.music.play(-1)

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
