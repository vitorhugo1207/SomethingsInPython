price = float(input('Qual o preço do produto: ').replace('R$', ''))
percentage = float(input('Qual o desconto em porcentagem: ').replace('%', ''))

discount = price * percentage / 100
total = price - (price * percentage / 100) 

print('O desconto de R${:.2f} é R${:.2f}, então o produto vai custar R${:.2f}.'.format(price, discount, total))