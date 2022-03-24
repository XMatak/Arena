import time
import random
from player_mod import player


hero = None

class colors: # barvy / colors
    PINK = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    STORY = '\033[1m'
    UNDERLINE = '\033[4m'

def decorateText(text):
    time.sleep(1)
    #print(f"{color}{text}{colors.ENDC}")
    # nefunguje v idlu :(
    print(text)
    

def stats(): # proste statistiky
#    decorateText(You sit down and think about it all. \nYou've killed {playerKills} creatures... and you died {playerDeaths} times.")
#    decorateText(Worth it?")
#    decorateText("You sit down and think about it all. \nYou've killed creatures..." + playerKills + "and you died" + playerDeaths + "times." )
    decorateText("Worth it?")
    decorateText("Maybe...")
          
def playerDeath(): # nahodna zprava o smrti
    deathMessages = ["A sword impales you. You died so early?", "Announcer: And a fatal hit! The human is defeated!", "An arrow pierces your skull, you wonder if it was an enemy, or a bystander.", "Weakling! he taunts you. No match for me!"]
    decorateText(deathMessages[random.randint(0,3)])
    decorateText("As the world fades around you, you see a face entering the arena.")
    decorateText("...you cannot quite make out who it belongs to.")
    
def startStory():   # prvni smrt? spis dialog a jestli je hrac ready
    decorateText("As you enter, an overwhelming sense of deja vu fills you.")
    decorateText("You've been here before, haven't you?")
    decorateText("A familiar voice greets you.")
    decorateText("Yo! Welcome challenger! Are you here for the arena?")
    if input("[y / n]: ") == "n":
        decorateText("Oh.")
        decorateText("Perish then-")
        playerDeath()
    else:
        decorateText("Whatever! Welcome!")
        time.sleep(2)

def selectHeroName():
    playerName = input("Just wondering, what is your name? ")
    time.sleep(1)
    print(playerName + "... cool!")
    time.sleep(1)
    return playerName

def selectHeroType():
    global hero
    heroName = selectHeroName()
    isNotHeroChosen = True
    while isNotHeroChosen:
        heroType = input("Who are you exactly? [mage / barb] ")
        if str(heroType) == "mage" or str(heroType) == "barb":
            hero = player(heroName, heroType)
            isNotHeroChosen = False
        else:
            decorateText("He asks you again, unsatisfied with your answer.")
            
    decorateText("Alright, we're all set!")
    decorateText("As you enter, the crown cheers. The announcer explains the rules, but you don't care.")
    decorateText("... you already know all of them.")
    decorateText("There are no rules.")

def getRandomEnemyName():
    enemyNames = ["Josef", "Gragas", "Blitzcrank", "Ash", "Doom", "Gangplank", "Halo", "Savathun", "Bowser", "Void", "'merica", "Wise Old Man", "Aatrox", "Tryndamere"]
    return enemyNames[random.randint(0,13)]

def getRandomEnemyHP():
    return(random.randint(110, 270))

def battle(heroName, heroType, enemyName, getEnemyHP): # bez objektoveho programovani, trochu prasarna
    isEnemyDead = False
    isPlayerDead = False
    heroHP = 10
    enemyHP = getEnemyHP
    while isEnemyDead == False and isPlayerDead == False:
        if heroType == "barb":
            decorateText("Choose your move:")
            playerMove = input("Attack / Super / Heal / Check [A/S/H/C] ")
            if playerMove == "A":
                attackText = ["You bonk him. The ding could be heard anywhere.", "You slap him. Ow.", "You dropkick him. He flew a bit.", "Spin to win is the strat, amiright?", "You swing your fists and manage to hit!"]
                decorateText(attackText[random.randint(0, 4)])
                enemyHP -= random.randint(10, 20)
            elif playerMove == "S":
                if heroHP >= 20:
                    decorateText("You concentrate.")
                    decorateText("... you don't feel angry enough.")
                else:
                    decorateText("The wrath of your ancestors calls upon you.")
                    decorateText("You feel the fury in your veins.")
                    decorateText("Your enemy is scared about what is going to happen.")
                    decorateText("He should be.")
                    decorateText("You start channeling your power:")
                    decorateText("The audience looks at you in anticipation.")
                    decorateText("You go full anime mode.")
                    decorateText("HIT!")
                    print("HIT!")
                    print("HIT!")
                    print("HIT!")
                    print("HIT!")
                    print("HIT!")
                    print("HIT!")
                    print("HIT!")
                    print("YOU ARE UNSTOPPABLE!")
                    print("HIT!")
                    print("HIT!")
                    print("HIT!")
                    print("HIt")
                    print("Hit")
                    print("hit")
                    decorateText("h i t")
                    decorateText("Too tired to continue.")
                    decorateText("Poor guy you think.")
                    decorateText("He looks really. really. REALLY not good.")
                    enemyHP -= random.randint(60, 100)
            elif playerMove == "H":
                decorateText("You concentrate on mending your wounds.")
                decorateText("You feel a little better.")
                heroHP += random.randint(20, 30)
            elif playerMove == "C":
                decorateText("What was his name?")
                decorateText(enemyName)
                decorateText("something like that...")
                decorateText("You thoroughly look at your opponent.")
                if enemyHP > 100:
                    decorateText("He looks scratchless.")
                elif enemyHP > 80:
                    decorateText("He looks fine.")
                elif enemyHP > 60:
                    decorateText("He looks wounded a bit.")
                elif enemyHP > 40:
                    decorateText("He looks beaten up.")
                elif enemyHP > 20:
                    decorateText("Yeah, he doesn't look good.")
                elif enemyHP > 0:
                    decorateText("He is a walking corpse.")
                else:
                    decorateText("He is dead.")
                    decorateText("You've been beating a dead horse.")
                    decorateText("You won.")
                    decorateText("... but at what costs?")
                    isEnemyDead = True
                            
        enemyMove = random.randint(1,4)
        if enemyMove == 1: # attack
            enemyAttackText = ["He pierces your skin with is dagger.", "He bonks you with his hammer.", "He shoots you with his bow.", "He shouts angrily and slaps you. Damn.", "He insults your family, emotional damage!"]
            decorateText(enemyAttackText[random.randint(0, 4)])
            heroHP -= random.randint(10, 20)
        elif enemyMove == 2: # super
            if enemyHP > 20:
                decorateText("He's just standing there. Menacingly.")
            else:
                decorateText("Something is wrong. You can feel it.")
                decorateText("Your opponent starts glowing like a star.")
                decorateText("It's almost burning your eyes.")
                decorateText(".")
                decorateText("..")
                decorateText("...")
                decorateText("He knocks you out.")
                decorateText(".")
                decorateText("..")
                decorateText("...")
                decorateText("You eventually wake up.")
                decorateText("Your entire body hurts. But you are not dead yet.")
                decorateText("...or are you?")
                playerHP -= random.randint(60,110)
        elif enemyMove == 3: # heal
            decorateText("He starts bandaging himself.")
            decorateText("You could stop him.")
            decorateText("But that's not fun.")
            enemyHP += random.randint(20,30)
        else:
            decorateText("He's looking at you.")
            decorateText("He shouts your name.")
            decorateText(heroName + ", more like coward!")
            if heroHP > 100:
                decorateText("You look scratchless.")
            elif heroHP > 80:
                decorateText("You look fine.")
            elif heroHP > 60:
                decorateText("You look wounded a bit.")
            elif heroHP > 40:
                decorateText("You look beaten up.")
            elif heroHP > 20:
                decorateText("Yeah, you don't look good.")
            elif heroHP > 0:
                decorateText("You are pretty much a walking corpse.")
            else:
                decorateText("You are dead.")
                decorateText("You've been given a chance until he confirms your kill.")
                decorateText("And yet. you failed.")
                decorateText("You lost.")
                isPlayerDead = True
                
                
                    
                

def mainLoop():
    #startStory()
    #battle(selectHeroName(), selectHeroType(), getRandomEnemyName(), getRandomEnemyHP())
    battle("pepa", "barb", "dummy", 150)

mainLoop()
