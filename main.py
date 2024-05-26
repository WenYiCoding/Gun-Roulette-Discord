#!1 Later: Seperate some function to other py file for GUI
#!2 User can type while time.sleep
#!3 may need seperate Main Menu from Program()
#!4 clear command not clean becoz \r

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
gunBullets = []

# Message Strings
askName = "Enter player name: "

# Functions
def clearCLI():
    os.system('cls||clear')

#> For item usage logic
def useItem(index = 999, playerItem = []):
    pass

#> For gun shooting logic
def shootGun(targetHP, bullets = []):
    result = ""
    print("You fired a gun ( -_•)▄︻テ══━一💥")
    bulletFired = bullets.pop(0)
    print("= ⁍ ")
    time.sleep(2) #!3
    if bulletFired == 1:
        targetHP -= 1
        result = f" 🩸 HIT"
    elif bulletFired == 0:
        result = " ⚬ Nothing happended"
    print(result)
    time.sleep(2) #!3
    return targetHP

#> Whole program logic
def program():
    clearCLI()
    player1 = Player(input("Enter player 1 name: "))
    player2 = Player(input("Enter player 2 name: "))

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

        print("Bullets:")
        print(gunBullets)

        for i in range(5,-1,-1):
            print(f"⁍⁍⁍ ▄︻テ══━一 Inserting bullets ({i})...", end="")
            print("\r", end="")
            time.sleep(1) #!3
        clearCLI() #!clear command not clean becoz \r

        random.shuffle(gunBullets)
        turnFlag = True
        while len(gunBullets) > 0:
                #!stupid hardcoded, will modulize VVV
            print(f"{player1.name}:{player1.hp} | {player2.name}:{player2.hp}\n")
            if turnFlag:
                print(f"< {player1.name}'s turn")
                print('='*TERMINAL_WIDTH)
                print(f"Items = {player1.items}")
            else:
                print(f"> {player2.name}'s turn")
                print('='*TERMINAL_WIDTH)
                print(f"Items = {player2.items}")
            
            print("[G]Use gun [1~8]Use item [X]Exit")
            actionChar = input(">>> ")
            clearCLI()

            if actionChar == "G":
                while True:
                    frontPlayer = player2.name if turnFlag else player1.name
                    frontHP = player2.hp if turnFlag else player1.hp

                    selfPlayer = player1.name if turnFlag else player2.name
                    selfHP = player1.hp if turnFlag else player2.hp

                    print("You are holding a gun ( -_•)▄︻テ══━一")
                    print('='*TERMINAL_WIDTH)
                    actionChar = input(f"[X]Shoot front: {frontPlayer} [O]Shoot self: {selfPlayer}\n>>> ")
                    clearCLI()

                    if actionChar == "X" or actionChar == "O":
                        break
                    else:
                        print("[X] Invalid input\n")

                if actionChar == "X":
                    targetHP = frontHP
                elif actionChar == "O":
                    targetHP = selfHP
                player1.hp = shootGun(targetHP, gunBullets)
                clearCLI()

                turnFlag = not(turnFlag)

            elif actionChar == "X":
                exit(0)
            elif actionChar.isdigit():
                itemIdx = int(actionChar)
                if (itemIdx > 0) and (itemIdx < 9):
                    useItem(itemIdx)
                else:
                    print("[X] Invalid input\n")
            else:
                print("[X] Invalid input\n")
                #!stupid hardcoded, will modulize ^^^
    
    if player1.hp < 1:
        print(f"☠️ {player1.name} is DEAD")
    if player2.hp < 1:
        print(f"☠️ {player2.name} is DEAD")

# MAIN
program()
while (input("Game ended! Play again? [Y/N]")):
    program()