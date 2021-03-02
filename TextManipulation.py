frase = '            Olá, eu sou o IkkiArtz                                  '

#print(frase[ Começo : Fim : Pular])
print(frase[::])

#Contar caracteres especificas
print(frase.upper().count('I'))

#Contar caracteres
print(len(frase))

#Tirar espaços na esquerda e direita
print(frase.strip())

#Tirar frases na esquerda
print(frase.rstrip())

#Tirar frases na direita
print(frase.lstrip())

#Substituir ou tirar partes especificas e para salvar é só jogar na variavel
print(frase.replace('Olá', 'Kk eae men'))
print(frase.replace('sou', ''))

#Se tem a palavra pesquisada True ou Falso
print('IkkiArtz' in frase)

#Ver em qual caractere esta a palavra pesquisada e se retornar '-1', significa que não tem a palavra pesquisada.
print(frase.find('IkkiArtz'))

#Dividir/transformar em lista
frase2 = frase.split()

#Sem o [] mostra a lista frase2
#Dicionar [qual str] [qual palavra]
print(frase2[4] [1])

#Outros
join()
frase.lower()
frase.upper()
frase.capitalize()
frase.title()