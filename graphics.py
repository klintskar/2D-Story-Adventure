from ctypes.wintypes import CHAR
from xml.dom.pulldom import CHARACTERS
import pygame
import wizard
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
########################################################################################
# Spritesheets
idle = pygame.image.load(spriteimage).convert_alpha()
idle_sprite_sheet = spritesheet.SpriteSheet(idle)
########################################################################################

def draw_textbox(text):
    WINWIDTH, WINHEIGHT = WIN.get_size()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    pygame.draw.rect(WIN, WHITE, pygame.Rect(0, (WINHEIGHT - (WINHEIGHT/6)), WINWIDTH, (WINHEIGHT/6)))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(10, ((WINHEIGHT - (WINHEIGHT/6))+10), (WINWIDTH-20), ((WINHEIGHT/6)-20)))
    blit_text(WIN, text, (10, ((WINHEIGHT - (WINHEIGHT/6))+6)), font)

def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def draw_background(background):
    WINWIDTH, WINHEIGHT = WIN.get_size()
    background = pygame.transform.scale(background, (WINWIDTH, WINHEIGHT))
    WIN.blit(background, (0, 0))

def draw_character(spritesheet, spritelist):
    global CHARACTERINDEX
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
        return True
    else:
        return False

def listinlist(list,index):
    return list[index]



def draw_window():
    draw_background(pygame.image.load("background1.png"))
    update_animate(wizard.wizardidle)
    draw_character(idle_sprite_sheet, wizard.wizardidle)
    draw_textbox("{Man} Once upon a time there was a lovely princess. But she had an enchantment upon her of a fearful sort which could only be broken by love's first kiss. She was locked away in a castle guarded by a terrible fire-breathing dragon. Many brave knigts had attempted to free her from this dreadful prison, but non prevailed. She waited in the dragon's keep in the highest room of the tallest tower for her true love and true love's first kiss. {Laughing} Like that's ever gonna happen. {Paper Rusting, Toilet Flushes} What a load of - ")
    pygame.display.update()

def graphics():
    
    clock = pygame.time.Clock()
    run = True
    n = 0
    
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
        
        draw_window()
                
    
    pygame.quit()


#This stops main from running if this file is imported
if __name__ == "__main__":
    graphics()