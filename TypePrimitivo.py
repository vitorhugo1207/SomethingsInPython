# Data extration
text = input('Digite alguma coisa: ')

# Data process
print('O tipo primitivo desse valor é', type(text))
print('Só tem espaços?', text.isspace())
print('É um número?', text.isnumeric())
print('É alfabético?', text.isalpha())