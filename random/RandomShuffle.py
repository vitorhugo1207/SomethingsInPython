from random import shuffle

thing1 = str(input('Uma coisa: '))
thing2 = str(input('Duas coisas: '))
thing3 = str(input('Terceira coisa: '))
thing4 = str(input('Quarta coisa: '))

deck = [thing1, thing2, thing3, thing4]

shuffle(deck)

print(deck)
