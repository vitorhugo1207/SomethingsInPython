name = input('Seu nome: ')

name1 = name.strip()
name2 = name1.find(' ')

print(name.capitalize()[:name2])