from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6), 'jogador2': randint(1,6),
        'jogador3': randint(1,6), 'jogador4': randint(1,6)}

print('Valores sorteados: ')

for k, v in jogo.items():
    print(f'O {k} tirou o número {v}')
    sleep(1)

ranking = []
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('  == RANKING ==:')

for i, v in enumerate(ranking):
    print(f'  {i+1} lugar: {v[0]} com {v[1]} pontos')
    sleep(1)


