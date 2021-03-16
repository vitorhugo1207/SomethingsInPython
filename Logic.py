from random import randrange
from os import startfile


def lin():
    print('-+' * 20)


def reset():
    startfile("C:/Users/Vitor/DocumentosTrue/!-Programação/Python/Project-Ikki/main.py")


dataLimit = 50

data = input('Which?\n-> ')
while True:
    if data == 'exit':
        break

    if data == 'sum':
        sum1 = int(randrange(0, dataLimit))
        sum2 = int(randrange(0, dataLimit))
        sumTotal = sum1 + sum2
        sumTotal = int(sumTotal)

        lin()
        totalSelf = input(f'What sum of {sum1} + {sum2}: ')

        if totalSelf == 'exit':
            break

        totalSelf = int(totalSelf)

        if totalSelf == sumTotal:
            print(f'You is right: {sum1} + {sum2} = {sumTotal}.')
        else:
            print(f'You is wrong: {sum1} + {sum2} = {sumTotal}.')

    if data == 'subtraction':
        sum1 = int(randrange(0, dataLimit))
        sum2 = int(randrange(0, dataLimit))
        sumTotal = sum1 - sum2

        lin()
        totalSelf = input(f'What subtracton of {sum1} - {sum2}: ')

        if totalSelf == 'exit':
            break

        totalSelf = int(totalSelf)

        if totalSelf == sumTotal:
            print(f'You is right: {sum1} - {sum2} = {sumTotal}.')
        else:
            print(f'You is wrong: {sum1} - {sum2} = {sumTotal}.')

    if data == 'multiplication':
        sum1 = int(randrange(0, dataLimit))
        sum2 = int(randrange(0, dataLimit))
        sumTotal = sum1 * sum2

        lin()
        totalSelf = input(f'What sum of {sum1} * {sum2}: ')

        if totalSelf == 'exit':
            break

        totalSelf = int(totalSelf)

        if totalSelf == sumTotal:
            print(f'You is right: {sum1} * {sum2} = {sumTotal}.')
        else:
            print(f'You is wrong: {sum1} * {sum2} = {sumTotal}.')

    if data == 'division':
        sum1 = int(randrange(0, dataLimit))
        sum2 = int(randrange(0, dataLimit))
        sumTotal = sum1 / sum2

        lin()
        totalSelf = input(f'What sum of {sum1} / {sum2}: ')

        if totalSelf == 'exit':
            break

        totalSelf = int(totalSelf)

        if totalSelf == sumTotal:
            print(f'You is right: {sum1} / {sum2} = {sumTotal}.')
        else:
            print(f'You is wrong: {sum1} / {sum2} = {sumTotal}.')
