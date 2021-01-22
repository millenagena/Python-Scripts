from random import randint
maior = menor = 0
numeros = (randint(0,20), randint(0,20), randint(0,20), randint(0,20), randint(0,20))
print(f'Os números sorteados foram:')

for n in numeros:
    print(f'{n} ', end='' )
print(f'\nO maior número é {max(numeros)}')
print(f'O menor número é {min(numeros)}')