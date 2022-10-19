import pygame

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

wizardtext = ["{Man} Once upon a time there was a lovely princess. But she had an enchantment upon her of a fearful sort which could only be broken by love's first kiss. She was locked away in a castle guarded by a terrible fire-breathing dragon. Many brave knigts had attempted to free her from this dreadful prison, but non prevailed. She waited in the dragon's keep in the highest room of the tallest tower for her true love and true love's first kiss. {Laughing} Like that's ever gonna happen. {Paper Rusting, Toilet Flushes} What a load of - ", "Hejsan Svejsan", "Hejdå"]

heart = "heart.png"

# Alla object på våra maps och vart dom ligger plaserade
startobjects = ["wizardpath.png",(0,0.5)]
eastobjects = []
combatobjects = []

rubbish1 = []
rubbish2 = []
rubbish3 = []
rubbish4 = []

forestfadetext = ["Detta är en skog. Skogibogitog","Oj ett träd","Shit en kebab!"]
startfadetext = []
wizardfadetext = []
combatfadetext = ["Nu ska du slåss mot ett skelet"]

#Picture, HP, DMG, Name, kill function number
skeleton = [pygame.image.load("skeleton.png"),10,1,"Skeleton",80085]

# index 0 = bild, index 1-4 = om kan gå åt det hållet, index 5-8 namn för hållen, index 9 = information om området
north = []
combat = [pygame.image.load("cell.png"),True,False,False,False,"","","","","combat",pygame.image.load("fade.png"),combatfadetext,combatobjects,skeleton]
wizard = [pygame.image.load("background1.png"),False,True,False,False,"","Conversation over","","","textbox",pygame.image.load("fade.png"),wizardfadetext,wizardtext,"idle.png",wizardidle]
east = [pygame.image.load("woods.png"),False,False,False,True,"North","East","South","Start","path",pygame.image.load("fade.png"),forestfadetext,eastobjects]
start = [pygame.image.load("pathbackground.png"),False,True,True,True,"North","East","Combat","Wizard","path",pygame.image.load("fade.png"),startfadetext,startobjects]

def kill(number):
       if number == 80085:
              global combat
              combat[9] = "path"
              combatfadetext = []

# Kartan
map = [[rubbish1,north,rubbish2],
       [wizard,start,east],
       [rubbish3,combat,rubbish4]]
mapcheckpoint = []

def save_checkpoint():
       global mapcheckpoint
       mapcheckpoint = map.copy()

def load_checkpoint():
       global map
       map = mapcheckpoint
