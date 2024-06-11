# Library imports
import os
import random
import time

# Global variables
TERMINAL_WIDTH = os.get_terminal_size()[0]
CLI_HORIZONTAL_LINE = '='*TERMINAL_WIDTH

# Message Strings
askName = "Enter player's name\n[!] Enter empty name to become bot\n"
askRounds = "How many rounds do you want to play?"
inputArrow = ">>> "
insertBullets = "⁍⁍⁍ ▄︻テ══━一 Inserting bullets... "
turnOptions = "[G]Use gun [1~8]Use item [X]Exit"
gunHolding = "You are holding a gun ( -_•)▄︻テ══━一\nWho you are going to shoot?"
gunFired = "You fired a gun ( -_•)▄︻テ══━一💥"
bulletFly = "= ⁍ "
hit = " 🩸 HIT"
nothing = " ⚬ Nothing happended"
isDead = " is DEAD ☠️"
playAgain = "Game ended! Play again? [Y]Yes [N]No"
invalidInput = "[!] Invalid input\n"
noSuchItem = "[!] No such item"
winIcon = "⭕"
loseIcon = "❌"

# Message Strings: Items
magnifierDesc = "Check the current bullet"
magnifierUsed = "Gun is checked and the bullet is viewed"
mobilePhoneDesc = "Someone hint you about the gun's future"
mobileUsed = "Mobile is telling you about the gun"
inverterDesc = "Invert the type of the current bullet"
inverterUsed = "The inverter is used, the bullet is now reversed"
sawDesc = "Double the damage"
sawUsed = "The saw is used, current bullet will shoot out x2 damage"
sodaDesc = "Pump the gun and ejects current bullet out"
gunUsed = "Gun is pumped and a bullet come out"
borrowGunDesc = "Borrow a gun with one bullet, 50% chance that bullet is live"
borrowGunUsed = "Someone gave you a gun but the bullet is unknown"
cigaretteDesc = "Gain 1 hp without side effects, relax"
cigaretteUsed = "Light the cigarette and relax"
pillDesc = "50% gain 3 hp, 50% lose 2 hp"
pillUsed = "Take a pill, let's see whats next... "
maxHealth = "The health is maxed out, putting the item back"
handcuffDesc = "Make front player skips their next turn"
handcuffUsed = "Front player is cuffed and cannot make the next move"
adrenalineDesc = "Steal 1 item from front player and use immediately"
adrenalineUsed = "Quick! Steal something already"
adrenalineNotUsed = "No items to steal"
adrenalineGiveUp = "Give up stealing? What a nice person you are"
cannotSteal = "This item cannot be stolen"

# Player structure
class Player:
    def __init__(self, name):
        self.playerType = "BOT" if (name == "") else "User"
        self.name = name if self.playerType == "User" else "BOT"
        self.hp = 10
        self.items = []
        self.roundHistory = []
    def __repr__(self) -> str:
        return f"Player type: {self.playerType}\nPlayer name: {self.name}\nPlayer HP: {self.hp}\nPlayer items: {self.items}\nPlayer win history: {self.roundHistory}\n"

# Item structures
class Item:
    def __init__(self):
        self.description = ""
    def __repr__(self):
        return self.__class__.__name__
    def __str__(self):
        return self.description

class Magnifier(Item):
    def __init__(self):
        super().__init__()
        self.description = magnifierDesc
    def use(self, selfPlayer, frontPlayer, bullets, turnFlag):
        sendMessage(f"{magnifierUsed}\n{bullets[0]}")

class MobilePhone(Item):
    def __init__(self):
        super().__init__()
        self.description = mobilePhoneDesc
    def use(self, selfPlayer, frontPlayer, bullets, turnFlag):
        whichBullet = random.randint(2,len(bullets))
        bulletLive = "LIVE" if bullets[(whichBullet -1)] == 1 else "BLANK"
        sendMessage(f"{mobileUsed}\nThe bullet no. {whichBullet} is {bulletLive}")

class Inverter(Item):
    def __init__(self):
        super().__init__()
        self.description = inverterDesc
    def use(self, selfPlayer, frontPlayer, bullets, turnFlag):
        bullets[0] = 1 if bullets[0] == 0 else 0
        sendMessage(inverterUsed)

class Saw(Item):
    def __init__(self):
        super().__init__()
        self.description = sawDesc
    def use(self, selfPlayer, frontPlayer, bullets, turnFlag):
        bullets[0] = bullets[0] * 2
        sendMessage(sawUsed)

class Beer(Item):
    def __init__(self):
        super().__init__()
        self.description = sodaDesc
    def use(self, selfPlayer, frontPlayer, bullets, turnFlag):
        sendMessage(f"{gunUsed}\n{bullets.pop(0)}")

class BorrowGun(Item):
    def __init__(self):
        super().__init__()
        self.description = borrowGunDesc
    def use(self, selfPlayer, frontPlayer, bullets, turnFlag):
        sendMessage(borrowGunUsed)
        bullets.insert(0, random.randint(0,1))

class Cigarette(Item):
    def __init__(self):
        super().__init__()
        self.description = cigaretteDesc
    def use(self, selfPlayer, frontPlayer, bullets, turnFlag):
        if selfPlayer.hp < 10:
            selfPlayer.hp = selfPlayer.hp + 1
            sendMessage(cigaretteUsed)
        else:
            selfPlayer.items.append(Cigarette())
            sendMessage(maxHealth)
    
class Pill(Item):
    def __init__(self):
        super().__init__()
        self.description = pillDesc
    def use(self, selfPlayer, frontPlayer, bullets, turnFlag):
        if selfPlayer.hp < 10:
            hpGain = 3 if random.randint(0,1) == 1 else -2
            selfPlayer.hp = selfPlayer.hp + hpGain
            sendMessage(pillUsed)
        else:
            selfPlayer.items.append(Pill())
            sendMessage(maxHealth)
    
#!!NOT COMPLETE
class Handcuff(Item):
    def __init__(self):
        super().__init__()
        self.description = handcuffDesc
    def use(self, selfPlayer, frontPlayer, bullets, turnFlag):
        sendMessage(handcuffUsed)
        return ["turnFlag", turnFlag +1]

class Adrenaline(Item):
    def __init__(self):
        super().__init__()
        self.description = adrenalineDesc
    def use(self, selfPlayer, frontPlayer, bullets, turnFlag):
        if len(frontPlayer.items) <= 0:
            sendMessage(adrenalineNotUsed)
            selfPlayer.items.append(Adrenaline())
        else:
            sendMessage(adrenalineUsed)
            while True:
                for idx, eachItem in enumerate(frontPlayer.items):
                    sendMessage(f"[{1+ idx}] {eachItem.__class__.__name__}")
                sendMessage("[X] Give up stealing")
                inputKey = waitInput(inputArrow)
                clearCLI()
                if inputKey.isdigit():
                    inputKey = int(inputKey)
                    if (inputKey > 0 and inputKey <= len(frontPlayer.items)):
                        itemName = frontPlayer.items[inputKey -1].__class__.__name__
                        if itemName == "Adrenaline":
                            sendMessage(cannotSteal)
                        elif (itemName == "Cigarette" or itemName == "Pill") and selfPlayer.hp >= 10:
                            sendMessage(maxHealth)
                        else:
                            frontPlayer.items.pop(inputKey -1).use(selfPlayer, frontPlayer, bullets)
                            return
                    else:
                        sendMessage(invalidInput)
                elif inputKey == "X":
                    sendMessage(adrenalineGiveUp)
                    return
                else:
                    sendMessage(invalidInput)

#> Generate an item
def createItem(idx):
    if idx == 0:
        return Magnifier()
    elif idx == 1:
        return MobilePhone()
    elif idx == 2:
        return Inverter()
    elif idx == 3:
        return Saw()
    elif idx == 4:
        return Beer()
    elif idx == 5:
        return BorrowGun()
    elif idx == 6:
        return Cigarette()
    elif idx == 7:
        return Pill()
    elif idx == 8:
        return Handcuff()
    elif idx == 9:
        return Adrenaline()
    else:
        sendMessage(noSuchItem)

#> Clear terminal output
def clearCLI():
    os.system('cls||clear')

#> Initialize the player
def initPlayer():
    players = []
    for i in range(1,3):
        players.append(Player(waitInput(f"[Player {i}] {askName}{inputArrow}")))
        clearCLI()
    return players

#> Set rounds to play
def setRounds():
    number = ""
    while not(number.isdigit()):
        sendMessage(number, end="")
        number = waitInput(f"{askRounds}\n{inputArrow}")
        clearCLI()
        number = number if number.isdigit() else invalidInput
    return int(number)

#> Reload gun
def gunReload():
    bullets = []

    for i in range(random.randint(2,8)):
        if i == 0:
            bullets.append(1)
        elif i == 1:
            bullets.append(0)
        else:
            bullets.append(random.randint(0,1))
    random.shuffle(bullets)

    sendMessage(f"Bullets:\n{bullets}")

    for i in range(5,-1,-1):
        sendMessage(f"{insertBullets}({i})\r", end="")
        time.sleep(1) #!3

    random.shuffle(bullets)
    clearCLI() #!4

    return bullets

#> Reset player health
def resetHealth(players):
    for player in players:
        player.hp = 10
    return players

#> Hold gun
def holdGun(selfPlayer, frontPlayer, bullets):
    inputKey = ""

    sendMessage(gunHolding)
    while inputKey != "X" and inputKey != "O":
        sendMessage(invalidInput if inputKey != "" else "")
        inputKey = waitInput(f"[X]Shoot front: {frontPlayer.name} [O]Shoot self: {selfPlayer.name}\n{inputArrow}")
        clearCLI()
    if inputKey == "X":
        result = shootGun(frontPlayer.hp, bullets)
        frontPlayer.hp = result[0]
        return result[1]
    elif inputKey == "O":
        result = shootGun(selfPlayer.hp, bullets)
        selfPlayer.hp = result[0]
        return not(result[1])

#> Shoot gun
def shootGun(targetHP, bullets):
    hitFlag = False
    sendMessage(gunFired)
    bulletFired = bullets.pop(0)
    sendMessage(bulletFly)
    time.sleep(2) #!3
    if (bulletFired == 1) or (bulletFired == 2):
        targetHP -= bulletFired
        sendMessage(hit)
        hitFlag = True
    elif bulletFired == 0:
        sendMessage(nothing)
    time.sleep(2) #!3
    clearCLI()
    return [targetHP, hitFlag]

#> Item usage logic
def useItem(index, selfPlayer, frontPlayer, bullets, turnFlag):
    if index > (len(selfPlayer.items)):
        sendMessage(noSuchItem)
    else:
        inputKey = ""
        while True:
            sendMessage(selfPlayer.items[(index - 1)])
            inputKey = waitInput(f"[O]Use [X]Keep\n{inputArrow}")
            clearCLI()
            if inputKey == "O" or inputKey == "X":
                break
            else:
                sendMessage(invalidInput)
        if inputKey == "X":
            return
        elif inputKey == "O":
            item = selfPlayer.items.pop((index - 1))
            result = item.use(selfPlayer, frontPlayer, bullets, turnFlag)
            time.sleep(2)
            clearCLI()
            return result

#> Turn logic
def round(players):
    bullets = []
    turnFlag = 1
    arrowFlag = True
    firstCycleFlag = True

    selfPlayer = players[0]
    frontPlayer = players[1]

    while True:
        #> Check player health, give win
        for idx, player in enumerate(players):
            if player.hp <= 0:
                sendMessage(f"{player.name}{isDead}\n")
                time.sleep(2) #!3
                player.roundHistory.append(loseIcon)

                idx = idx + 1
                idx = 0 if idx >= len(players) else idx

                players[idx].roundHistory.append(winIcon)

                return

        #> Check bullets and run cycle
        if len(bullets) <= 0:
            if firstCycleFlag:
                firstCycleFlag = not(firstCycleFlag)
            else:
                for player in players:
                    player.items.append(createItem(random.randint(0,9)))
            bullets = gunReload()
        
        sendMessage(f"{players[0].name}:{players[0].hp} | {players[1].name}:{players[1].hp}\n")

        if turnFlag == 0:
            tempPlayer = selfPlayer
            selfPlayer = frontPlayer
            frontPlayer = tempPlayer
            turnFlag = turnFlag +1
            arrowFlag = not(arrowFlag)

        sendMessage("Front player's items: ", end="")
        for eachItem in frontPlayer.items:
            sendMessage(eachItem.__class__.__name__, end=", ")
        sendMessage()

        sendMessage("<- " if arrowFlag else "-> ", end="")
        sendMessage(f"{selfPlayer.name}'s turn\n{CLI_HORIZONTAL_LINE}\nItems = ", end="")
        for eachItem in selfPlayer.items:
            sendMessage(eachItem.__class__.__name__, end=", ")
        sendMessage()
        
        inputKey = waitInput(f"{turnOptions}\n{inputArrow}")
        clearCLI()

        if inputKey == "G":
            extraTurn = holdGun(selfPlayer, frontPlayer, bullets)
            turnFlag = turnFlag if extraTurn else turnFlag -1

        elif inputKey == "X":
            exit(0)

        elif inputKey.isdigit():
            itemIdx = int(inputKey)
            if (itemIdx > 0) and (itemIdx < 9):
                result = useItem(itemIdx, selfPlayer, frontPlayer, bullets, turnFlag)
                if result[0] == "turnFlag":
                    turnFlag = result[1]
            else:
                sendMessage(invalidInput)

        else:
            sendMessage(invalidInput)

#> Whole program logic
def program():
    while True:
        clearCLI()
        players = initPlayer()

        for i in range(0,setRounds()):
            sendMessage(f"Round {1+i}\n{CLI_HORIZONTAL_LINE}")

            players = resetHealth(players)
            round(players)

            sendMessage("Wins")
            for player in players:
                sendMessage(f"{player.name}: {player.roundHistory}")
            sendMessage()
        
        while True:
            inputKey = waitInput(f"{playAgain}\n{inputArrow}")
            clearCLI()
            if inputKey == "N":
                exit(0)
            elif inputKey == "Y":
                break
            else:
                sendMessage(invalidInput)

def waitInput(string):
    pass

def sendMessage(string):
    pass