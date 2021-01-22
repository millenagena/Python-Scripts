'''n = int(input('Informe um número inteiro: '))
num = n
fat = 1
while n != 1:
    fat = fat*n
    n -= 1
print(f'O fatorial do número {num} é {fat}')'''

n = int(input('Informe um número inteiro: '))
num = n
fat = 1
print(f'Calculando {num}! = ', end='')
while n != 0:
    print(f'{n}', end='')
    fat = fat*n
    n -= 1
    if n == 0:
        print('', end='')
    else:
        print(' x ', end='')
print(f' = {fat}')