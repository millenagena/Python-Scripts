n = int(input('Informe um número: '))
cont = 0

for c in range (2, n):
    if n%c == 0:
        cont = 1

if cont == 1:
    print('\nO número informado NÃO É PRIMO!')
else:
    print('\nO número informado É PRIMO!')
