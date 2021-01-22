from random import randint
print('----------------------------------------------------')
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('----------------------------------------------------')
num = randint(0, 5)
n = int(input('\nEm qual número eu pensei? '))
print('PROCESSANDO...')
if n == num:
    print('\nPARABÉNS!! Você acertou o número e venceu o jogo.')
else:
    print(f'\nERRADO!! Eu pensei no número {num} não em {n}')