import random


data = input('Which?\n-> ')
while True:
    if data == 'exit':
        break

    if data == 'sum':
        sum1 = int(random.randrange(0, 50))
        sum2 = int(random.randrange(0, 50))
        sumTotal = sum1 + sum2

        totalSelf = input(f'What sum of {sum1} + {sum2}: ')

        if totalSelf == sumTotal:
            print(f'You is right: {sum1} + {sum2} = {sumTotal}.')
        if totalSelf == 'exit':
            break
        else:
            print(f'You is wrong: {sum1} + {sum2} = {sumTotal}.')

    if data == 'subtracton':
        sum1 = int(random.randrange(0, 50))
        sum2 = int(random.randrange(0, 50))
        sumTotal = sum1 - sum2

        totalSelf = input(f'What subtracton of {sum1} - {sum2}: ')

        if totalSelf == sumTotal:
            print(f'You is right: {sum1} - {sum2} = {sumTotal}.')
        if totalSelf == 'exit':
            break
        else:
            print(f'You is wrong: {sum1} - {sum2} = {sumTotal}.')

    if data == 'multiplication':
        sum1 = int(random.randrange(0, 50))
        sum2 = int(random.randrange(0, 50))
        sumTotal = sum1 * sum2

        totalSelf = input(f'What sum of {sum1} * {sum2}: ')

        if totalSelf == sumTotal:
            print(f'You is right: {sum1} * {sum2} = {sumTotal}.')
        if totalSelf == 'exit':
            break
        else:
            print(f'You is wrong: {sum1} * {sum2} = {sumTotal}.')

    if data == 'division':
        sum1 = int(random.randrange(0, 50))
        sum2 = int(random.randrange(0, 50))
        sumTotal = sum1 / sum2

        totalSelf = input(f'What sum of {sum1} / {sum2}: ')

        if totalSelf == sumTotal:
            print(f'You is right: {sum1} / {sum2} = {sumTotal}.')
        if totalSelf == 'exit':
            break
        else:
            print(f'You is wrong: {sum1} / {sum2} = {sumTotal}.')
