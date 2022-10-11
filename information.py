import pygame

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

rubbish1 = []
rubbish2 = []
rubbish3 = []
rubbish4 = []

# index 0 = bild, index 1-4 = om kan gå åt det hållet, index 5-8 namn för hållet, index 9 = information om hållet
north = []
south = []
wizard = [pygame.image.load("background1.png"),False,True,False,False,"","Conversation over","","","textbox"]
east = []
start = [pygame.image.load("pathbackground.jpg"),False,False,False,True,"North","East","South","Wizard","path"]

map = [[rubbish1,north,rubbish2],
       [wizard,start,east],
       [rubbish3,south,rubbish4]]