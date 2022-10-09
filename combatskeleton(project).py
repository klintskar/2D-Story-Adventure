import random
def damage(attacked):
    pass#player or enemy
def getenemyhp():
    pass
def getplayerhp():
    return 1
def openinventory():
    pass
def combat(player, enemy):
    getplayerhp()
    getenemyhp
    clickedbutton= none
    if clicked==fightbutton:
        attack(enemy)#player attacking enemy
        attack(player)#enemy attack player
    elif clicked==inventory:
        pass
        #inventoryeffect
    elif clicked==run:
        print("enemy gets one last attack before you run")
        attack(player)
        
def attack(attacked):
    hitormiss=random.randint(1,3)
    if hitormiss<3:
        print("The attack missed")
    else:
        print("it hit")
        damage(attacked)
    
def playervictory(enemy):
    print(f"you defeated {enemy}")
combatactive=True
def initiatecombat():
    while enemyhp>0 and playerhp>0:
        combat(player, enemy)
    if enemyhp<1:
        playervictory(enemy)
    elif playerhp<1:
        reset()
initiatecombat()
    
    
    