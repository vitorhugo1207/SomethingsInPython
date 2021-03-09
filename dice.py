from random import *
import time


def dice():
    diceRoll = (randrange(0, 20))
    print(f'Your roll: {diceRoll}')

def diceMain(self):
    roll: int = (randrange(0, diceT))
    print(f'Your roll: {roll}')


if __name__ == '__main__':
    while True:
        # Data extraction
        print('-' * 20)
        dice = str(input('-> ').replace('d', ''))

        if dice in 'exit':
            break

        # Extraction amount times loop
        diceA = dice[:1]
        # Extraction interval of draw
        diceT = dice[1:]

        # Bonus extraction
        if '+' in dice:
            diceMore = dice.find('+')
            rollBonus = dice[diceMore:].replace('+', '')
            rollBonus = int(rollBonus)
            print(rollBonus)

        # Int
        diceT = int(diceT)
        diceA = int(diceA)

        # Self
        diceT = self=diceT
        diceA = self=diceA

        # Loop if diceA > 1
        for X in range(diceA):
            diceMain(self)
        # time.sleep(3.0)
