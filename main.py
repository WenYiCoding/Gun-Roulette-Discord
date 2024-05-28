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

# Global variables
TERMINAL_WIDTH = os.get_terminal_size()[0]
CLI_HORIZONTAL_LINE = '='*TERMINAL_WIDTH

# Message Strings
askName = "Enter player's name\n[!] Enter empty name to become bot\n"
inputArrow = ">>> "
insertBullets = "⁍⁍⁍ ▄︻テ══━一 Inserting bullets... "
gunHolding = "You are holding a gun ( -_•)▄︻テ══━一"
gunFired = "You fired a gun ( -_•)▄︻テ══━一💥"
bulletFly = "= ⁍ "
hit = " 🩸 HIT"
nothing = " ⚬ Nothing happended"
isDead = " is DEAD ☠️"
playAgain = "Game ended! Play again? [Y/N]"
invalidInput = "[X] Invalid input\n"

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
        number = input(f"How many rounds do you want to play?\n{inputArrow}")
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

#> Turn logic
def turn():
    pass

#> Round logic
def round(players):
    players = resetHealth(players)
    while True:
        for player in players:
            if player.hp <= 0:
                print(f"{player.name}{isDead}")
                time.sleep(2) #!3
                return
        
        turnFlag = True
        bullets = gunReload()

#> Item usage logic
def useItem(index = 999, playerItem = []):
    pass

#> Shoot gun
def shootGun(targetHP, bullets = []):
    print(gunFired)
    bulletFired = bullets.pop(0)
    print(bulletFly)
    time.sleep(2) #!3
    if bulletFired == 1:
        targetHP -= 1
        print(hit)
    elif bulletFired == 0:
        print(nothing)
    time.sleep(2) #!3
    return targetHP

#> Whole program logic
def program():
    clearCLI()
    players = initPlayer()

    for i in range(0,setRounds()):
        print(f"Round {1+i}")
        round(players)

###############################################
    os._exit(0)
    turnFlag = True

    turn()

    for player in players:
        player.name

    while (player1Hp > 0) or (player2Hp > 0):
        

        random.shuffle(gunBullets)
        turnFlag = True
        while len(gunBullets) > 0:
            print(f"{player1Name}:{player1Hp} | {player2Name}:{player2Hp}\n")

            frontPlayer = player2 if turnFlag else player1
            selfPlayer = player1 if turnFlag else player2
            print("< " if turnFlag else "> ", end="")
            print(f"{selfPlayer.name}'s turn\n{CLI_HORIZONTAL_LINE}\nItems = {selfPlayer.items}")
            
            print("[G]Use gun [1~8]Use item [X]Exit")
            actionChar = input(inputArrow)
            clearCLI()

            if actionChar == "G":
                while True:
                    print(gunHolding)
                    print(CLI_HORIZONTAL_LINE)
                    actionChar = input(f"[X]Shoot front: {frontPlayer.name} [O]Shoot self: {selfPlayer.name}\n{inputArrow}")
                    clearCLI()

                    if actionChar != "X" and actionChar != "O":
                        print(invalidInput)
                    else:
                        break

                if actionChar == "X":
                    frontPlayer.hp = shootGun(frontPlayer.hp, gunBullets)
                elif actionChar == "O":
                    selfPlayer.hp = shootGun(selfPlayer.hp, gunBullets)
                clearCLI()

                turnFlag = not(turnFlag)

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
                #!stupid hardcoded, will modulize ^^^
    
    if player1.hp < 1:
        print(f"☠️ {player1Name} is DEAD")
    if player2.hp < 1:
        print(f"☠️ {player2Name} is DEAD")

# MAIN
program()
while (input(playAgain)):
    program()