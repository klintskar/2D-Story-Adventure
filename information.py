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

rubbish1 = []
rubbish2 = []
rubbish3 = []
rubbish4 = []

# index 0 = bild, index 1-4 = om kan gå åt det hållet, index 5-8 namn för hållen, index 9 = information om området
north = []
south = []
wizard = [pygame.image.load("background1.png"),False,True,False,False,"","Conversation over","","","textbox",pygame.image.load("fade.png"),wizardtext,"idle.png",wizardidle]
east = [pygame.image.load("woods.png"),False,False,False,True,"North","East","South","Start","path",pygame.image.load("fade.png"),eastobjects]
start = [pygame.image.load("pathbackground.jpg"),False,True,False,True,"North","East","South","Wizard","path",pygame.image.load("fade.png"),startobjects]

# Kartan
map = [[rubbish1,north,rubbish2],
       [wizard,start,east],
       [rubbish3,south,rubbish4]]
