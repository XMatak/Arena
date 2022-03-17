import time
import random

playerHealth = None
playerMana = None
playerClass = None
playerName = None

enemyHealth = None
enemyMana = None

def stats(): # proste statistiky
    print(f"You sit down and think about it all. \nYou've killed {playerKills} creatures... and you died {playerDeaths} times.")
    time.sleep(2)
    print("Worth it?")
    time.sleep(2)
    print("Maybe...")
          
def playerDeath(): # nahodna zprava o smrti
    time.sleep(2)
    deathMessages = ["A sword impales you. You died so early?", "Announcer: And a fatal hit! The human is defeated!", "An arrow pierces your skull, you wonder if it was an enemy, or a bystander.", "Weakling! he taunts you. No match for me!"]
    print(deathMessages[random.randint(0,3)])
    time.sleep(3)
    print("As the world fades around you, you see a face entering the arena.")
    time.sleep(1)
    print("...you cannot quite make out who it belongs to.")
    time.sleep(2)
    global playerDeaths
    playerDeaths += 1
    
def startArena():   # prvni smrt? spis dialog a jestli je hrac ready
    print("As you enter, an overwhelming sense of deja vu fills you.")
    time.sleep(2)
    print("You've been here before, haven't you?")
    time.sleep(2)
    print("A familiar voice greets you.")
    time.sleep(2)
    print("Yo! Welcome challenger! Are you here for the arena?")
    if input("[y / n]: ") == "n":
        time.sleep(1)
        print("Oh.")
        time.sleep(1)
        print("Perish then-")
        playerDeath()
    else:
        print("Whatever! Welcome!")
        time.sleep(2)
        trueArena()

def trueArena():
    playerName = input("Just tell me your name, ok?")
    time.sleep(2)
    playerClass = input(f"{playerName}, cool! Now tell me, what are you? [mage / barb]")
    time.sleep(2)
    batt


        
