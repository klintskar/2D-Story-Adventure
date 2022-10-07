import pygame
import spritesheet
import os

########################################################################################
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rat Simulator")
########################################################################################
UGLYGREEN = (30, 50, 40)
ratX, ratY = 300, 100
FPS = 30
VEL = 10
RATSIZEX, RATSIZEY = 60, 45
BLACK = (0, 0, 0)

sprite_sheet_image = pygame.image.load('arts.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
########################################################################################
RatUp = [sprite_sheet.get_image(0, 3, 32, 32, 4, BLACK),
      sprite_sheet.get_image(1, 3, 32, 32, 4, BLACK),
      sprite_sheet.get_image(2, 3, 32, 32, 4, BLACK),]

RatDown = [sprite_sheet.get_image(0, 0, 32, 32, 4, BLACK),
      sprite_sheet.get_image(1, 0, 32, 32, 4, BLACK),
      sprite_sheet.get_image(2, 0, 32, 32, 4, BLACK),]

RatLeft = [sprite_sheet.get_image(0, 1, 32, 32, 4, BLACK),
      sprite_sheet.get_image(1, 1, 32, 32, 4, BLACK),
      sprite_sheet.get_image(2, 1, 32, 32, 4, BLACK),]

RatRight = [sprite_sheet.get_image(0, 2, 32, 32, 4, BLACK),
      sprite_sheet.get_image(1, 2, 32, 32, 4, BLACK),
      sprite_sheet.get_image(2, 2, 32, 32, 4, BLACK),]

Ratindex = 0
Ratpos = 0

Catindex = 0

CatDown = [sprite_sheet.get_image(6, 0, 32, 32, 8, BLACK),
      sprite_sheet.get_image(7, 0, 32, 32, 8, BLACK),
      sprite_sheet.get_image(8, 0, 32, 32, 8, BLACK),]

RAT_IMAGE = sprite_sheet.get_image(0, 0, 32, 32, 4, BLACK)
CAT_IMAGE = sprite_sheet.get_image(6, 0, 32, 32, 8, BLACK)

########################################################################################

def animatecat(n):
    if n%5 == 0:
        global CAT_IMAGE
        global Catindex
        if Catindex < 2:
            Catindex += 1
            CAT_IMAGE = CatDown[Catindex]
        else:
            Catindex = 0
            CAT_IMAGE = CatDown[Catindex]

def animaterat(n):
    n += 1
    if n%5 == 0:
        global RAT_IMAGE
        global Ratindex
        if Ratpos == 0:
            if Ratindex < 2:
                Ratindex += 1
                RAT_IMAGE = RatUp[Ratindex]
            else:
                Ratindex = 0
                RAT_IMAGE = RatUp[Ratindex]
        elif Ratpos == 1:
            if Ratindex < 2:
                Ratindex += 1
                RAT_IMAGE = RatDown[Ratindex]
            else:
                Ratindex = 0
                RAT_IMAGE = RatDown[Ratindex]
        elif Ratpos == 2:
            if Ratindex < 2:
                Ratindex += 1
                RAT_IMAGE = RatLeft[Ratindex]
            else:
                Ratindex = 0
                RAT_IMAGE = RatLeft[Ratindex]
        elif Ratpos == 3:
            if Ratindex < 2:
                Ratindex += 1
                RAT_IMAGE = RatRight[Ratindex]
            else:
                Ratindex = 0
                RAT_IMAGE = RatRight[Ratindex]
    return n

def draw_window(rat, cat):
    
    WIN.fill(UGLYGREEN) #Update background
    WIN.blit(RAT_IMAGE, (rat.x, rat.y))
    WIN.blit(CAT_IMAGE, (cat.x, cat.y))
    pygame.display.update()

def RatGame():
    rat = pygame.Rect(100, 300, RATSIZEX, RATSIZEY)
    cat = pygame.Rect(600, 150, RATSIZEX, RATSIZEY)
    
    clock = pygame.time.Clock()
    run = True
    n = 0
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        keys_pressed = pygame.key.get_pressed()
        global Ratpos
        if keys_pressed[pygame.K_w]:
            rat.y -= VEL
            Ratpos = 0
        elif keys_pressed[pygame.K_s]:
            rat.y += VEL
            Ratpos = 1
        elif keys_pressed[pygame.K_a]:
            rat.x -= VEL
            Ratpos = 2
        elif keys_pressed[pygame.K_d]:
            rat.x += VEL
            Ratpos = 3
        
        draw_window(rat, cat)
        n = animaterat(n)
        animatecat(n)
                
    
    pygame.quit()


#This stops main from running if this file is imported
if __name__ == "__main__":
    RatGame()