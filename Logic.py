import random
import os


def lin():
    print('-+' * 20)


def reset():
    os.startfile("C:/Users/Vitor/DocumentosTrue/!-Programação/Python/Project-Ikki/main.py")
    exit()


dataLimit = 50

data = input('Which?\n-> ')
while True:
    if data == 'exit':
        break

    if data == 'sum':
        sum1 = int(random.randrange(0, dataLimit))
        sum2 = int(random.randrange(0, dataLimit))
        sumTotal = sum1 + sum2
        sumTotal = int(sumTotal)

        lin()
        totalSelf = input(f'What sum of {sum1} + {sum2}: ')

        if totalSelf == 'exit':
            break
        if totalSelf == 'reset':
            reset()

        totalSelf = int(totalSelf)

        if totalSelf == sumTotal:
            print(f'You is right: {sum1} + {sum2} = {sumTotal}.')
        else:
            print(f'You is wrong: {sum1} + {sum2} = {sumTotal}.')

    if data == 'subtracton':
        sum1 = int(random.randrange(0, dataLimit))
        sum2 = int(random.randrange(0, dataLimit))
        sumTotal = sum1 - sum2

        lin()
        totalSelf = input(f'What subtracton of {sum1} - {sum2}: ')

        if totalSelf == 'exit':
            break
        if totalSelf == 'reset':
            reset()

        totalSelf = int(totalSelf)

        if totalSelf == sumTotal:
            print(f'You is right: {sum1} - {sum2} = {sumTotal}.')
        if totalSelf == 'exit':
            break
        else:
            print(f'You is wrong: {sum1} - {sum2} = {sumTotal}.')

    if data == 'multiplication':
        sum1 = int(random.randrange(0, dataLimit))
        sum2 = int(random.randrange(0, dataLimit))
        sumTotal = sum1 * sum2

        lin()
        totalSelf = input(f'What sum of {sum1} * {sum2}: ')

        if totalSelf == 'exit':
            break
        if totalSelf == 'reset':
            reset()

        totalSelf = int(totalSelf)

        if totalSelf == sumTotal:
            print(f'You is right: {sum1} * {sum2} = {sumTotal}.')
        if totalSelf == 'exit':
            break
        else:
            print(f'You is wrong: {sum1} * {sum2} = {sumTotal}.')

    if data == 'division':
        sum1 = int(random.randrange(0, dataLimit))
        sum2 = int(random.randrange(0, dataLimit))
        sumTotal = sum1 / sum2

        lin()
        totalSelf = input(f'What sum of {sum1} / {sum2}: ')

        if totalSelf == 'exit':
            break
        if totalSelf == 'reset':
            reset()

        totalSelf = int(totalSelf)

        if totalSelf == sumTotal:
            print(f'You is right: {sum1} / {sum2} = {sumTotal}.')
        if totalSelf == 'exit':
            break
        else:
            print(f'You is wrong: {sum1} / {sum2} = {sumTotal}.')

    if data == 'reset':
        reset()
