import json

class Chatbot():
    def __init__(self, nome):
        memoria = open(nome+'.json','r')
        self.nome = nome
        self.conhecidos = json.load(memoria)
        memoria.close()
        self.historico = []
    
    def escuta(self):
        frase = input('>: ')
        frase = frase.lower()
        frase = frase.replace('é' , 'eh')
        return frase
    
    def pensa(self, frase):
        if frase == 'oi':
            return 'Olá, qual o seu nome?'
        if self.historico[-1] == 'Olá, qual o seu nome?':
            nome = self.pegaNome(frase)
            frase = self.respondeNome(nome)
            return frase
        return 'Não entendi'

    def pegaNome(self, nome):
        if 'o meu nome eh ' in nome:
            nome = nome[14: ]
        
        nome = nome.title()
        return nome
    
    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = 'Eaew '
        else:
            frase = 'Muito prazer '
            self.conhecidos.append(nome)
            memoria = open(self.nome+'.json','w')
            json.dump(self.conhecidos,memoria)
            memoria.close()

        return frase+nome

    def fala(self,frase):
        print(frase)
        self.historico.append(frase)