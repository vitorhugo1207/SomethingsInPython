from random import *
import time

def d20():
    d20 = (randrange(0, 20))
    print(f'Your roll: {d20}')

if __name__ == '__main__':
    d20()
    time.sleep(3.0)