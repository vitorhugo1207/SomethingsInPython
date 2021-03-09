num = int(input('Digite algum numero: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analisando numero {num}')

if u > 0:
    print(f'Unidade: {u}')

if d > 0:
    print(f'Dezena: {d}')

if c > 0:
    print(f'Centena: {c}')

if m > 0:
    print(f'Milhar: {m}')
