import pygame
import information
import spritesheet
import time

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
spriteimage = "idle.png"
start = time.time()
keystart = time.time()
keys_pressed = None
textbox = ["{Man} Once upon a time there was a lovely princess. But she had an enchantment upon her of a fearful sort which could only be broken by love's first kiss. She was locked away in a castle guarded by a terrible fire-breathing dragon. Many brave knigts had attempted to free her from this dreadful prison, but non prevailed. She waited in the dragon's keep in the highest room of the tallest tower for her true love and true love's first kiss. {Laughing} Like that's ever gonna happen. {Paper Rusting, Toilet Flushes} What a load of - ", "Hejsan Svejsan", "Hejdå"]
textboxindex = 0
currentlocationx = 1
currentlocationy = 1
########################################################################################
# Spritesheets
idle = pygame.image.load(spriteimage).convert_alpha()
idle_sprite_sheet = spritesheet.SpriteSheet(idle)

########################################################################################
# Commonly used window functions

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
    global keystart
    global currentlocationx
    global currentlocationy
    keys_pressed = pygame.key.get_pressed()
    keynow = time.time()
    if keys_pressed[pygame.K_UP] and (keystart + 0.25) < (keynow):
        i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
        if i[1]:
            currentlocationy -= 1
        keystart = time.time()
    elif keys_pressed[pygame.K_RIGHT] and (keystart + 0.25) < (keynow):
        i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
        if i[2]:
            currentlocationx += 1
        keystart = time.time()
    elif keys_pressed[pygame.K_DOWN] and (keystart + 0.25) < (keynow):
        i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
        if i[3]:
            currentlocationy += 1
        keystart = time.time()
    elif keys_pressed[pygame.K_LEFT] and (keystart + 0.25) < (keynow):
        i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
        if i[4]:
            currentlocationx -= 1
        keystart = time.time()

########################################################################################
# Specific draw textbox window functions

# Main function for textbox window
def draw_text_window():
    location_switch()
    next_text()
    draw_background()
    update_animate(information.wizardidle)
    draw_character(idle_sprite_sheet, information.wizardidle)
    draw_textbox(textbox[textboxindex])
    pygame.display.update()

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

# These 2 functions update the text shown in the textbox
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
            return x
        else:
            x = textboxindex
            textboxindex += 1
            return x
    else:
        x = textboxindex
        textboxindex += 1
        return x

########################################################################################

def draw_choose_path():
    draw_background()
    location_switch()
    pygame.display.update()

########################################################################################
# Pygame start function

def graphics():
    
    pygame.mixer.init()
    pygame.mixer.music.load("game_music.wav")
    pygame.mixer.music.play(-1)
    
    clock = pygame.time.Clock()
    run = True
    global key_pressed
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_ESCAPE]:
            pygame.quit()
        elif keys_pressed[pygame.K_w]:
            pass
        
        i = listinlist(listinlist(information.map,currentlocationy),currentlocationx)
        if i[9] == "textbox":
            draw_text_window()
        if i[9] == "path":
            draw_choose_path()          
    
    pygame.quit()

#This stops main from running if this file is imported
if __name__ == "__main__":
    graphics()
