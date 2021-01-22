from random import randint
from time import sleep

def sortear(n, lst):
    print(f'Sorteando {n} valores da lista:')
    for v in range(0, n):
        num = (randint(0, 10))
        print(num, end=' ')
        sleep(0.5)
        lst.append(num)
    print('PRONTO!')


def somapar(list):
    spar = 0
    for k, v in enumerate(list):
        if v % 2 == 0:
            spar += v
    print(f'A soma dos valores pares da lista {list} é {spar}')



#Programa Principal
lista = []
print('-='*30)
sortear(5, lista)
somapar(lista)
print('-='*30)