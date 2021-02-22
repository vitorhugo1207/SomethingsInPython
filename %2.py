values = float(input('Qual o valor: ').format('R$', ''))
percentage = float(input('Qual a porcentagem: ').format('%', ''))

increase = values * percentage / 100
total = values + (values * percentage / 100)

print('O aumento {:.1f}% de R${:.2f} é R${:.2f}, então o total é R${:.2f}'
.format(percentage, values, increase, total))

