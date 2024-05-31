## Notes
#!1 Later: Seperate some function to other py file for GUI
#!2 User can type while time.sleep
#!3 may need seperate Main Menu from Program()
#!4 clear command not clean becoz \r
#!5 starting bullets does not force at least one 0 and 1
#!6 not in use

## Plans
#? more player support
#? item modding support
#? rules configuration

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
handcuffDesc = "Make front player skips their next turn"
handcuffUsed = ""
adrenalineDesc = "Steal 1 item from front player and use immediately"
adrenalineUsed = ""

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
#!!NOT COMPLETE
class Item:
    def __init__(self):
        self.description = ""
    def __repr__(self):
        return self.description

class Magnifier(Item):
    def __init__(self):
        super().__init__()
        self.description = magnifierDesc
    def use(self, selfPlayer, frontPlayer, bullets):
        print(f"{magnifierUsed}\n{bullets[0]}")

class MobilePhone(Item):
    def __init__(self):
        super().__init__()
        self.description = mobilePhoneDesc
    def use(self, selfPlayer, frontPlayer, bullets):
        whichBullet = random.randint(1,len(bullets))
        print(f"{mobileUsed}\nThe bullet no. {whichBullet} is {bullets[whichBullet]}")

class Inverter(Item):
    def __init__(self):
        super().__init__()
        self.description = inverterDesc
    def use(self, selfPlayer, frontPlayer, bullets):
        bullets[0] = 1 if bullets[0] == 0 else 0
        print(inverterUsed)

class Saw(Item):
    def __init__(self):
        super().__init__()
        self.description = sawDesc
    def use(self, selfPlayer, frontPlayer, bullets):
        bullets[0] = bullets[0] * 2
        print(sawUsed)

class Soda(Item):
    def __init__(self):
        super().__init__()
        self.description = sodaDesc
    def use(self, selfPlayer, frontPlayer, bullets):
        print(f"{gunUsed}\n{bullets.pop(0)}")

class BorrowGun(Item):
    def __init__(self):
        super().__init__()
        self.description = borrowGunDesc
    def use(self, selfPlayer, frontPlayer, bullets):
        print(borrowGunUsed)
        return bullets.insert(0, random.randint(0,1))
    
class Cigarette(Item):
    def __init__(self):
        super().__init__()
        self.description = cigaretteDesc
    def use(self, selfPlayer, frontPlayer, bullets):
        selfPlayer.hp = selfPlayer.hp + 1
        print(cigaretteUsed)
    
class Pill(Item):
    def __init__(self):
        super().__init__()
        self.description = pillDesc
    def use(self, selfPlayer, frontPlayer, bullets):
        hpGain = 3 if random.randint(0,1) == 1 else -2
        selfPlayer.hp = selfPlayer.hp + hpGain
        print(pillUsed)
    
class Handcuff(Item):
    def __init__(self):
        super().__init__()
        self.description = handcuffDesc
    def use(self, selfPlayer, frontPlayer, bullets):
        pass
        print()

class Adrenaline(Item):
    def __init__(self):
        super().__init__()
        self.description = adrenalineDesc
    def use(self, selfPlayer, frontPlayer, bullets):
        pass
        print()
#!!NOT COMPLETE

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
        return Soda()
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
        print(noSuchItem)

#> Clear terminal output
def clearCLI():
    os.system('cls||clear')

#> Initialize the player
def initPlayer():
    players = []
    for i in range(1,3):
        players.append(Player(input(f"[Player {i}] {askName}{inputArrow}")))
        clearCLI()
    return players

#> Set rounds to play
def setRounds():
    number = ""
    while not(number.isdigit()):
        print(number, end="")
        number = input(f"{askRounds}\n{inputArrow}")
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

    print(f"Bullets:\n{bullets}")

    for i in range(5,-1,-1):
        print(f"{insertBullets}({i})\r", end="")
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
    actionKey = ""

    print(gunHolding)
    while actionKey != "X" and actionKey != "O":
        print(invalidInput if actionKey != "" else "")
        actionKey = input(f"[X]Shoot front: {frontPlayer.name} [O]Shoot self: {selfPlayer.name}\n{inputArrow}")
        clearCLI()
    if actionKey == "X":
        result = shootGun(frontPlayer.hp, bullets)
        frontPlayer.hp = result[0]
        return result[1]
    elif actionKey == "O":
        result = shootGun(selfPlayer.hp, bullets)
        selfPlayer.hp = result[0]
        return not(result[1])

#> Shoot gun
def shootGun(targetHP, bullets):
    hitFlag = False
    print(gunFired)
    bulletFired = bullets.pop(0)
    print(bulletFly)
    time.sleep(2) #!3
    if (bulletFired == 1) or (bulletFired == 2):
        targetHP -= bulletFired
        print(hit)
        hitFlag = True
    elif bulletFired == 0:
        print(nothing)
    time.sleep(2) #!3
    clearCLI()
    return [targetHP, hitFlag]

#> Item usage logic
def useItem(index, selfPlayer, frontPlayer, bullets):
    if index > (len(selfPlayer.items)):
        print(noSuchItem)
    else:
        inputKey = ""
        while True:
            print(selfPlayer.items[(index - 1)])
            inputKey = input(f"[O]Use [X]Keep\n{inputArrow}")
            clearCLI()
            if inputKey == "O" or inputKey == "X":
                break
            else:
                print(invalidInput)
        if inputKey == "X":
            return
        elif inputKey == "O":
            selfPlayer.items[(index - 1)].use(selfPlayer, frontPlayer, bullets)
            time.sleep(2)
            clearCLI()

#> Player target logic #!6
""" def targetPlayer(players):
    while True:
        for idx, player in enumerate(players):
            print(f"[{1 + idx}] {player.name} (HP = {player.hp})")
        inputKey = input(inputArrow)
        if inputKey.isdigit():
            inputKey = int(inputKey)
            if (inputKey > 0) and (inputKey <= len(players)):
                inputKey = inputKey -1
                return players[inputKey]
        print(invalidInput)
 """

#> Turn logic
def round(players):
    bullets = []
    turnFlag = True
    firstCycleFlag = True

    while True:
        #> Check player health, give win
        for idx, player in enumerate(players):
            player.items.append(createItem(random.randint(0,9))) #!!DEBUG
            if player.hp <= 0:
                print(f"{player.name}{isDead}\n")
                time.sleep(2) #!3
                player.roundHistory.append(loseIcon)

                idx = idx + 1
                idx = 0 if idx >= len(players) else idx

                players[idx].roundHistory.append(winIcon)

                return

        #> Check bullets
        if len(bullets) <= 0:
            if firstCycleFlag:
                firstCycleFlag = not(firstCycleFlag)
            else:
                for player in players:
                    player.items.append(createItem(random.randint(0,9)))
            bullets = gunReload()
        
        print(f"{players[0].name}:{players[0].hp} | {players[1].name}:{players[1].hp}\n")

        selfPlayer = players[0] if turnFlag else players[1]
        frontPlayer = players[1] if turnFlag else players[0]

        print("< " if turnFlag else "> ", end="")
        print(f"{selfPlayer.name}'s turn\n{CLI_HORIZONTAL_LINE}\nItems = ", end="")
        for eachItem in selfPlayer.items:
            print(eachItem.__class__.__name__, end=", ")
        print()
        
        actionChar = input(f"{turnOptions}\n{inputArrow}")
        clearCLI()

        if actionChar == "G":
            extraTurn = holdGun(selfPlayer, frontPlayer, bullets)
            turnFlag = turnFlag if extraTurn else not(turnFlag)

        elif actionChar == "X":
            exit(0)

        elif actionChar.isdigit():
            itemIdx = int(actionChar)
            if (itemIdx > 0) and (itemIdx < 9):
                useItem(itemIdx, selfPlayer, frontPlayer, bullets)
            else:
                print(invalidInput)

        else:
            print(invalidInput)

#> Whole program logic
def program():
    while True:
        clearCLI()
        players = initPlayer()

        for i in range(0,setRounds()):
            print(f"Round {1+i}\n{CLI_HORIZONTAL_LINE}")

            players = resetHealth(players)
            round(players)

            print("Wins")
            for player in players:
                print(f"{player.name}: {player.roundHistory}")
            print()
        
        while True:
            inputKey = input(f"{playAgain}\n{inputArrow}")
            clearCLI()
            if inputKey == "N":
                exit(0)
            elif inputKey == "Y":
                break
            else:
                print(invalidInput)

# MAIN
program()