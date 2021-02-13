import subprocess
import os
import json
import time
from downloadTime import projectdownload as pd

# Fazer um sistema de dados

#_______________________________________________________________________

def lin():
    print('-' * 30)

def info():
    output1 = 'Esse programa esta na versão: 0'
    output2 = 'Desenvolvido por IkkiArtz.'
    output3 = 'Criado no dia 18/10/2020'
    print(output1)
    print(output2)
    print(output3)

def timecont2():
    time.sleep(2.0)

def abrir():
    print('O que quer abrir?')
    respabrir = input('-> ')
    respabrir = respabrir.lower()
    try:
        subprocess.Popen(respabrir)
        lin()
        output5 = 'Aberto!'
        print(output5)
        lin()
    except:
        file = open('Arquivo'+'.json','r')
        file.close
        # output6 = 'Não entendi!'
        # print(output6)
        lin()

def aprende():
    # a função "aprende" só está guardando um item.
    chave = input('Digite a frase: ')
    valor = input('Digite o caminho: ')
    chave = chave.lower()
    valor = valor.lower()
    try:
        file = open('Arquivo.json','w')
        json.dump({chave:valor}, file, indent=2)
        file.close
        print('Aprendido!')
        # file = open('Arquivo'+'.json','r')
        # Arquivo = json.load(file)
        # file.close
        # print(Arquivo)
    except:
        print('Ocorreu um ERRO.')
    finally:
        file.close
    lin()

def arquivo():
    try:
        file = open('Arquivo.json', 'r')
        file.close
        print ('Arquivo já existente')
    except FileNotFoundError:
        file = open('Arquivo.json', 'w+')
        file.close
        print('Arquivo criado!')

def zerar():
    print('Tem certeza que deseja apagar a memoria do script?')
    output7 = input('-> ')
    output7 = output7.lower()
    output7 = output7.replace(' ','')
    if output7 == 'sim':
        file = open('Arquivo.json', 'w+')
        file.close
        lin()
        print('Memoria do script apagada!')
    elif output7 == 'não':
        lin()
        print('Ok, memoria do script não apagada!')
    else:
        lin()
        print('Não entendi!')

def apagar():
    lin()
    print('Tem certeza que deseja apagar o arquivo da memoria do script?')
    output4 = input('-> ')
    output4 = output4.lower
    output4 = output4.replace(' ','')
    if output4 == 'sim':
        os.remove('Arquivo.json')
        lin()
        print('Arquivo da memoria do script apagado!')
    elif output4 == 'não':
        lin()
        print('Ok, o arquivo da memoria do script não foi apagada!')
    else:
        lin()
        print('Não entendi!')

class main():
    lin()
    print('Hi, what must do?')
    texto = input('-> ')
    texto = texto.lower()
    texto = texto.replace(' ','')
    lin()

    if texto == 'open':
        abrir()

    elif texto == 'lear':
        aprende()

    elif texto == 'info':
        info()

    elif texto == 'file':
        arquivo()

    elif texto == 'zerar':
        zerar()

    elif texto == 'eraser':
        apagar()

    elif texto == 'download time':
        pd()

    else:
        try:
            print(eval(texto))
        except:
            print('Não entendi!')
            lin()
    timecont2()
