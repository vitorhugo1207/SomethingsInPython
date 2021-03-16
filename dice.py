from random import *
from datetime import datetime
from time import sleep

# Made by IkkiArtz


def diceMain():
    roll = randrange(diceMin, diceT) # diceMin (Minimum) between diceT (Total)
    return roll # Return variable scroll for list

def lin():
    print('-+' * 20)

def error():
    print('I am sorry, did not understood. Type "help" for instructions.')
    sleep(5)
    exit()


if __name__ == '__main__':
    while True:
        # __Data extraction__
        lin() # Line
        dice = str(input('-> ').replace(' ', '').lower()) # Data extraction, remove space and letter in lower


        if dice == 'exit': # Break the Loop
            break

        if dice == 'help': # Help
            pass


        # __Dice scroll times__
        diceFindD = dice.find('d') # Find "d" position
        diceA = dice[:diceFindD].replace('d', '') # Extraction time of dice roll and remove "d"
        if diceA == '': # If not was defined time of dice roll at variable
            diceA = 1 # Roll the dice one time

        diceT = dice[diceFindD:].replace('d', '') # Extraction interval of draw


        # __Bonus extraction__
        if '+' in dice:
            diceMore = dice.find('+') # Find position of the scroll bonus
            rollBonus = dice[diceMore:].replace('+', '') # Remove the dice and "+"
            diceT = dice[diceMore:].replace('+', '') # Remove the dice and "+"
            rollBonus = int(rollBonus) # Str for Int

        if '-' in dice:
            diceLess = dice.find('-') # Find position of the scroll bonus
            rollBonus = dice[diceLess:].replace('-', '') # Remove the dice and "-"
            diceT = dice[diceLess:].replace('-', '') # Remove the dice and "-"
            rollBonus = int(rollBonus) # Str for Int


        # __Str for Int__
        try:
            diceT = int(diceT) + 1
            diceA = int(diceA)
        except:
            error()


        # __Created a variable diceMin__
        diceMin = 0 # The minimum for start scroll dice


        rollList = [] # Created a list


        # __Loop of scroll dice time__
        for X in range(diceA):
            rollList.append(diceMain()) # Call def and save data at list


        # __Sum List of dice roll and roll bonus__
        if '+' in dice:
            rollTotal = sum(rollList) + rollBonus # Sum list and roll
            rollList.append(f'+{rollBonus}') # Add rollBonus at list
            rollBonus = '' # Clean variable rollBonus
        else:
            rollTotal = sum(rollList) # Sum if not has rollBonus

        if '-' in dice:
            rollTotal = sum(rollList) - rollBonus # subtract list and roll
            rollList.append(f'-{rollBonus}') # Add rollBonus at list
            rollBonus = '' # Clean variable rollBonus
        else:
            rollTotal = sum(rollList) # Sum if not has rollBonus


        # __Data show__
        timenow = datetime.now() # Acquiring time of scrolling dice
        time = timenow.strftime('%d/%m/%y at %H:%M:%S') # Formatting time of scrolling dice
        print(time) # Show time of scrolling dice
        if len(rollList) >= 1:
            print(f'List of dice roll: {rollList}') # Show list of scroll dice and bonus
        print(f'Total of dice roll: {rollTotal}') # Show total of scroll dice and bonus
