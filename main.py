#!1 Later: Seperate some function to other py file for GUI
#!2 User can type while time.sleep
#!3 may need seperate Main Menu from Program()
#!4 clear command not clean becoz \r
#!5 starting bullets does not force at least one 0 and 1

# Library imports
import os
import random
import time

# Class construction
class Player:
    def __init__(self, name):
        self.playerType = "BOT" if (name == "") else "User"
        self.name = name
        self.hp = 10
        self.items = []
        self.roundHistory = []

# Global variables
TERMINAL_WIDTH = os.get_terminal_size()[0]
CLI_HORIZONTAL_LINE = '='*TERMINAL_WIDTH

# Message Strings
askName = "Enter player's name\n[!] Enter empty name to become bot\n"
askRounds = "How many rounds do you want to play?"
inputArrow = ">>> "
insertBullets = "⁍⁍⁍ ▄︻テ══━一 Inserting bullets... "
turnOptions = "[G]Use gun [1~8]Use item [X]Exit"
gunHolding = "You are holding a gun ( -_•)▄︻テ══━一"
gunFired = "You fired a gun ( -_•)▄︻テ══━一💥"
bulletFly = "= ⁍ "
hit = " 🩸 HIT"
nothing = " ⚬ Nothing happended"
isDead = " is DEAD ☠️"
playAgain = "Game ended! Play again? [Y/N]"
invalidInput = "[!] Invalid input\n"

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
    if bulletFired == 1:
        targetHP -= 1
        print(hit)
        hitFlag = True
    elif bulletFired == 0:
        print(nothing)
    time.sleep(2) #!3
    clearCLI()
    return [targetHP, hitFlag]

#> Item usage logic
def useItem(index = 999, playerItem = []):
    pass

#> Turn logic
def round(players):
    bullets = []
    turnFlag = True

    while True:
        #> Check player health, give win
        for idx, player in enumerate(players):
            if player.hp < 10:
                print(f"{player.name}{isDead}\n")
                time.sleep(2) #!3
                player.roundHistory.append("❌")

                idx = idx + 1
                idx = 0 if idx >= len(players) else idx

                players[idx].roundHistory.append("⭕")

                return

        #> Check bullets
        if len(bullets) <= 0:
            bullets = gunReload()
        
        print(f"{players[0].name}:{players[0].hp} | {players[1].name}:{players[1].hp}\n")

        selfPlayer = players[0] if turnFlag else players[1]
        frontPlayer = players[1] if turnFlag else players[0]

        print("< " if turnFlag else "> ", end="")
        print(f"{selfPlayer.name}'s turn\n{CLI_HORIZONTAL_LINE}\nItems = {selfPlayer.items}")
        
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
                useItem(itemIdx)
            else:
                print(invalidInput)

        else:
            print(invalidInput)

#> Whole program logic
def program():
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

# MAIN
program()
while (input(f"{playAgain}\n{inputArrow}")):
    program()