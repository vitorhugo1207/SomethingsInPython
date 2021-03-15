from random import *
from datetime import datetime

# Tratar erros


def diceMain():
    roll = randrange(diceMin, diceT) # diceMin (Minimum) between diceT (Total)
    return roll


if __name__ == '__main__':
    while True:
        # Data extraction
        print('-+' * 20) # Line
        dice = str(input('-> ').replace('d', '')).replace(' ', '') # Data extraction, remove "d" and space.

        if dice in 'exit': # Break the Loop
            break

        if dice == 'help':
            pass

        diceA = dice[:1] # Extraction amount times loop
        diceT = dice[1:] # Extraction interval of draw

        # Created a list
        rollList = []

        # Bonus extraction
        if '+' in dice:
            diceMore = dice.find('+') # Find position of the roll bonus
            rollBonus = dice[diceMore:].replace('+', '') # Remove the dice and "+"
            diceT = dice[diceMore:].replace('+', '') # Remove the dice and "+"
            dice = dice[diceMore:].replace('+', '') # Remove the dice and "+"
            rollBonus = int(rollBonus) # Str for Int

        # Str for Int
        diceT = int(diceT)
        diceA = int(diceA)

        # Created a variable diceMin
        diceMin = 0 # The minimum for start roll dice

        # Loop if diceA > 1
        for X in range(diceA):
            rollList.append(diceMain()) # Call def and save data at list

        # Sum List of dice roll and roll bonus
        try:
            rollTotal = sum(rollList) + rollBonus # Try sum list and roll
            rollList.append(f'+{rollBonus}') # Add rollBonus at list
            rollBonus = '' # Clean variable rollBonus
        except:
            rollTotal = sum(rollList) # Sum if not has rollBonus

        # Data show
        timenow = datetime.now()
        time = timenow.strftime('%d/%m/%y at %H:%M:%S')
        print(time)
        print(f'List of dice roll: {rollList}')
        print(f'Total of dice roll: {rollTotal}')
        # time.sleep(3.0)
