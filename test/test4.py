import json

chave = input('Chave: ')
valor = input('Valor: ')

with open('test4j.json', 'w') as json_file:
    json.dump({chave:valor}, json_file, indent=4)

