import random

def codeFinder():
    carac = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'ç', 'A', 'B', 'C',
             'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'Y', 'Z', 'Ç', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', '0', '!', '@', '#','$', '%', '*',
             '(', ')', '{', '}', '^', '¨', '?', ' '
             ] # 78

    code = ''

    while(code != find):
        code = ''
        for x in find:
            found = carac[random.randint(0, 77)]
            code = str(found) + str(code)
        print(code)

    print('Code found:',code)

if __name__ == '__main__':
    find = input('-> ')
    codeFinder()