from random import randint
nsorteados = []
lista = []
num = qntd = cont = 0
j = 0
print('-='*30)
print(f'{"JOGO DA MEGA SENA":^60}')
print('-='*30)
qntd = int(input('Quantos jogos você deseja fazer? '))
print()
while j != qntd:
    while cont < 6:
        num = randint(0, 60)
        if num not in nsorteados:
            nsorteados.append(num)
            cont += 1
        if cont == 6:
            nsorteados.sort()
            lista.append(nsorteados[:])
            print(f'{j+1}° Jogo: {nsorteados}')
            nsorteados.clear()
    cont = 0
    j += 1
