import time
import random

def decorateText(text):
    #print(f"{color}{text}{colors.ENDC}")
    # nefunguje v idlu :(
    input(text)
          
def playerDeath(): # nahodna zprava o smrti, momentalne moc nevyuzita, patch vyjde v dohledne dobe
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

def selectHeroName(): # proste se zepta hrace na jmeno
    playerName = input("Just wondering, what is your name? ")
    print(playerName + "... cool!")
    return playerName

def selectHeroType():  # zepta se na typ hrace, mag je i podle dialogu momentalne nenacodenej
    global hero
    isNotHeroChosen = True
    while isNotHeroChosen:
        heroType = input("Who are you exactly? [mage / barb] ")
        if str(heroType) == "barb":
            isNotHeroChosen = False
        elif str(heroType) == "mage":
            decorateText("Mages are not allowed in this arena.")
            decorateText("You get a feeling that they have not been coded yet.")
        else:
            decorateText("He asks you again, unsatisfied with your answer.")
            
    decorateText("Alright, we're all set!")
    decorateText("As you enter, the crown cheers. The announcer explains the rules, but you don't care.")
    decorateText("... you already know all of them.")
    decorateText("There are no rules.")

def getRandomEnemyName(): # z listu vybere nahodne jmeno nepritele, jmeno jde pak zjistit pomoci akce Check
    enemyNames = ["Josef", "Gragas", "Blitzcrank", "Ash", "Doom", "Gangplank", "Halofungaming", "Savathun", "Bowser", "Void", "'merica", "Wise Old Man", "Aatrox", "Tryndamere"]
    return enemyNames[random.randint(0,13)]

def getRandomEnemyHP(): # vygeberuje nahodne nepratelske HP
    return(random.randint(110, 270))

def battle(heroName, heroType, enemyName, getEnemyHP): # bez objektoveho programovani, trochu prasarna
    isEnemyDead = False
    isPlayerDead = False
    heroHP = random.randint(100,150) # nahodne hp
    enemyHP = getEnemyHP
    while isEnemyDead == False and isPlayerDead == False: # cykli do doby, kdy jeden z bojovniku neumre
        print("Choose your move:")
        playerMove = input("Attack / Super / Heal / Check [A/S/H/C] ") # input
        if playerMove == "A": # mini utok hrace
            attackText = ["You bonk him. The ding could be heard anywhere.", "You slap him. Ow.", "You dropkick him. He flew a bit.", "Spin to win is the strat, amiright?", "You swing your fists and manage to hit!"]
            decorateText(attackText[random.randint(0, 4)])
            enemyHP -= random.randint(10, 20)
        elif playerMove == "S": # mega utok hrace
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
        elif playerMove == "H": # heal
            decorateText("You concentrate on mending your wounds.")
            decorateText("You feel a little better.")
            heroHP += random.randint(20, 30)
        elif playerMove == "C": # check, zjisti jmeno protivnika, jak je na tom se zivoty, v pripade, ze je nepritel mrtev, potvrdi smrt
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
                decorateText("A new challenger appears.")
                isEnemyDead = True
                            
        enemyMove = random.randint(1,4)
        if enemyMove == 1: # mini utok nepritele
            enemyAttackText = ["He pierces your skin with is dagger.", "He bonks you with his hammer.", "He shoots you with his bow.", "He shouts angrily and slaps you. Damn.", "He insults your family, emotional damage!"]
            decorateText(enemyAttackText[random.randint(0, 4)])
            heroHP -= random.randint(10, 20)
        elif enemyMove == 2: # mega utok nepritele
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
        elif enemyMove == 3: # heal protivnika
            decorateText("He starts bandaging himself.")
            decorateText("You could stop him.")
            decorateText("But that's not fun.")
            enemyHP += random.randint(20,30)
        else: # i kdyz elsem, checkne, rekne vase jmeno, v pripade, ze jste mrtev potvrdi kill
            decorateText("He's looking at you.")
            decorateText("He shouts your name.")
            decorateText(heroName + ", more like...")
            decorateText("He pauses for a second, thinking of an adequate roast.")
            roastList = ["Bumbo!", "coward!", "Stoopid!", "He can't think of anything. ", "Legend. He admires you?", "4chan user. That hurt -3hp"]
            decorateText(roastList[random.randint(0, 5)])
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
                decorateText("As the world fades around you a new face comes to the arena.")
                decorateText("He looks like...")
                decorateText("You!")
                decorateText("It starts to make sense now.")
                decorateText("Anyways, you're dead.")
                decorateText("And the guy is going to fight next.")
                decorateText("Or is it you?")
                decorateText("I don't know, I am lost.")

                isPlayerDead = True
                
                
                    
                
playerName = None
playerType = None
def mainLoop(): # drivery
    playTheGame = True
    startStory()
    playerName = selectHeroName()
    playerType = selectHeroType()
    battle(playerName, playerType, getRandomEnemyName(), getRandomEnemyHP())
    while playTheGame:
        if input("Do you want to play more? [any / n] ") == "n":
            decorateText("See you next time.")
        else:
            decorateText("Very well then.")
            battle(playerName, playerType, getRandomEnemyName(), getRandomEnemyHP())

mainLoop() # starter
