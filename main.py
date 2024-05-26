# Library imports
import os
import random
import time

# Global constants
TERMINAL_WIDTH = os.get_terminal_size()[0]


# Class construction
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 10
        self.items = []

# Global variables
    #!stupid hardcoded, will modulize VVV
player1Name = ""
player1HP = 10
player1Items = []

player2Name = ""
player2HP = 10
player2Items = []
    #!stupid hardcoded, will modulize ^^^

gunBullets = []

# Message Strings
askName = "Enter player name: "

# Functions
def renderCLI(): #!Not used
    pass

def clearCLI():
    os.system('cls||clear')

def useItem(index = 999, playerItem = []):
    pass

def shootGun(targetHP, bullets = []):
    result = ""
    print("You fired a gun ( -_•)▄︻テ══━一💥")
    bulletFired = bullets.pop(0)
    print("= ⁍ ")
    time.sleep(2) #!can type while waiting
    if bulletFired == 1:
        print(targetHP)
        
        targetHP -= 1
        result = f" 🩸 HIT"
        
        print(targetHP)
    elif bulletFired == 0:
        result = " ⚬ Nothing happended"
    time.sleep(2) #!can type while waiting
    return result

def program():
    clearCLI()
    player1 = Player(input("Enter player 1 name: "))
    player1Name = input("Enter player 1 name: ")
    #!CONTINUE
    player2 = Player(input("Enter player 1 name: "))
    player2Name = input("Enter player 2 name: ")

    while (player1HP > 0) or (player2HP > 0):
        for i in range(random.randint(2,8)):
            gunBullets.append(random.randint(0,1))
        random.shuffle(gunBullets)

        print("Bullets:")
        print(gunBullets)

        for i in range(5,-1,-1):
            print(f"⁍⁍⁍ ▄︻テ══━一 Inserting bullets ({i})...", end="")
            print("\r", end="")
            time.sleep(1) #!can type while waiting
        clearCLI() #!clear command not clean becoz \r

        random.shuffle(gunBullets)
        turnFlag = True
        while len(gunBullets) > 0:
                #!stupid hardcoded, will modulize VVV
            print(f"{player1Name}:{player1HP} | {player2Name}:{player2HP}\n")
            if turnFlag:
                print(f"< {player1Name}'s turn")
                print('='*TERMINAL_WIDTH)
                print(f"Items = {player1Items}")
            else:
                print(f"> {player2Name}'s turn")
                print('='*TERMINAL_WIDTH)
                print(f"Items = {player2Items}")
            
            print("[G]Use gun [1~8]Use item [X]Exit")
            actionChar = input(">>> ")
            clearCLI()

            if actionChar == "G":
                while True:
                    frontName = player2Name if turnFlag else player1Name
                    frontHP = player2HP if turnFlag else player1HP

                    selfName = player1Name if turnFlag else player2Name
                    selfHP = player1HP if turnFlag else player2HP

                    print("You are holding a gun ( -_•)▄︻テ══━一")
                    print('='*TERMINAL_WIDTH)
                    actionChar = input(f"[X]Shoot front: {frontName} [O]Shoot self: {selfName}\n>>> ")
                    clearCLI()

                    if actionChar == "X" or actionChar == "O":
                        break
                    else:
                        print("[X] Invalid input\n")

                if actionChar == "X":
                    targetHP = frontHP
                elif actionChar == "O":
                    targetHP = selfHP
                print(shootGun(targetHP, gunBullets))
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
    
    if player1HP < 1:
        print(f"☠️ {player1Name} is DEAD")
    if player2HP < 1:
        print(f"☠️ {player2Name} is DEAD")

# MAIN
""" program()
while (input("Game ended! Play again? [Y/N]")):
    program() """
player1 = Player(input("Enter player 1 name: "))
print(player1.name)
print(player1.hp)
print(player1.items)