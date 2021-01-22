from random import randint

itens = ['Pedra', 'Papel', 'Tesoura']
comp = randint(0,2)
op = int(input('''Suas ações: 
[0] Pedra
[1] Papel
[2] Tesoura
Qual sua jogada? '''))

print('\nSua jogada foi {}'.format(itens[op]))
print('A jogada do computador foi {}\n'.format(itens[comp]))
print('='*18)
if comp == op:
    print('EMPATE!')
elif comp == 0 and op == 2:
    print('COMPUTADOR VENCEU!')
elif comp == 2 and op == 0:
    print('JOGADOR VENCEU!')
elif comp == 0 and op == 1:
    print('JOGADOR VENCEU!')
elif comp == 1 and op == 0:
    print('COMPUTADOR VENCEU!')
elif comp == 1 and op == 2:
    print('JOGADOR VENCEU!')
elif comp == 2 and op == 1:
    print('COMPUTADOR VENCEU!')
else:
    print('JOGADA INVÁLIDA!')
print('='*18)
