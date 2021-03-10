from random import *
import time

# Mostrar a data da rolagem de dados, calcular o bonus e tratar erros


def dice():
    diceRoll = (randrange(0, 20))
    print(f'Your roll: {diceRoll}')

def diceMain():
    roll = randrange(0, diceT)
    return roll


if __name__ == '__main__':
    while True:
        # Data extraction
        print('-' * 20)
        dice = str(input('-> ').replace('d', '')).replace(' ', '') # Data extraction, remove "d" and spáce.

        if dice in 'exit': # Break the Loop
            break

        diceA = dice[:1] # Extraction amount times loop
        diceT = dice[1:] # Extraction interval of draw

        # Bonus extraction
        if '+' in dice:
            diceMore = dice.find('+')
            rollBonus = dice[diceMore:].replace('+', '')
            rollBonus = int(rollBonus)
            print(rollBonus)

        # Int
        diceT = int(diceT)
        diceA = int(diceA)

        # Created a list
        rollList = []

        # Loop if diceA > 1
        for X in range(diceA):
            rollList.append(diceMain())

        # Sum List of dice roll
        rollTotal = sum(rollList)

        # Show datas
        print(f'List of dice roll: {rollList}')
        print(f'Total of dice roll: {rollTotal}')

        # time.sleep(3.0)
