storyStage = {1:"start",2:"middle",3:"ending"} #Ändrar detta beroende på storyn. Varje stage är en checkpoint.
inventory = ["Potion", "Flowers", "Bomb"]

savefile = ""

#Spelvariabler
playerhealth = 10
stage = 0

#Grafikbaserade funktioner
def background():
    pass

def character():
    pass

def textbox():
    pass

def characterLocation(): #Ifall vi vill ha våran character på skärmen
    pass

#Logikbaserade funktioner
def removeItem(index):
    return inventory.pop(index)

def addItem():
    pass

def importSavefile():
    pass

def exportSavefile():
    pass

def resetStage(): #Återgår till senaste checkpoint
    pass

def getStage():
    global stage
    return stage

def setStage(index):
    global stage
    stage = index

def setPlayerhealth():
    pass

def getPlayerhealth():
    pass

