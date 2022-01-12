import random


def numGenarator():
    num = []
    for x in range(amount):
        for x in range(numAmount):
            num.append(random.randint(0, 9))
        print("".join(map(str, num)))
        num = []


if __name__ == '__main__':
    amount = int(input('-> '))
    numAmount = int(input('-> '))
    numGenarator()
