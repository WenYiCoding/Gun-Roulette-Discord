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
        self.name = name
        self.hp = 10
        self.items = []

# Global variables
TERMINAL_WIDTH = os.get_terminal_size()[0]
CLI_HORIZONTAL_LINE = '='*TERMINAL_WIDTH
gunBullets = []

# Message Strings
askName = "Enter player name: "
inputArrow = ">>> "
insertBullets = "⁍⁍⁍ ▄︻テ══━一 Inserting bullets... "
gunHolding = "You are holding a gun ( -_•)▄︻テ══━一"
gunFired = "You fired a gun ( -_•)▄︻テ══━一💥"
bulletFly = "= ⁍ "
hit = " 🩸 HIT"
nothing = " ⚬ Nothing happended"
enterPly1Name = "Enter player 1 name: "
enterPly2Name = "Enter player 2 name: "
playAgain = "Game ended! Play again? [Y/N]"
invalidInput = "[X] Invalid input\n"

# Functions
def clearCLI():
    os.system('cls||clear')

#> For item usage logic
def useItem(index = 999, playerItem = []):
    pass

#> For gun shooting logic
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
    player1 = Player(input(enterPly1Name))
    player2 = Player(input(enterPly2Name))

    player1Name = player1.name
    player1Hp = player1.hp
    player1Items = player1.items

    player2Name = player2.name
    player2Hp = player2.hp
    player2Items = player2.items

    while (player1Hp > 0) or (player2Hp > 0):
        for i in range(random.randint(2,8)):
            gunBullets.append(random.randint(0,1))
        random.shuffle(gunBullets)

        print(f"Bullets:\n{gunBullets}")

        for i in range(5,-1,-1):
            print(insertBullets, end="")
            print(f"({i})", end="")
            print("\r", end="")
            time.sleep(1) #!3
        clearCLI() #!clear command not clean becoz \r

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
                    actionChar = input(f"[X]Shoot front: {frontPlayer.name} [O]Shoot self: {selfPlayer.name}\n>>> ")
                    clearCLI()

                    if actionChar == "X" or actionChar == "O":
                        break
                    else:
                        print(invalidInput)

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