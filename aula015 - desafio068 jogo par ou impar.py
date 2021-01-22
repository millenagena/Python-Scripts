from random import randint
jogador = 0
comp = soma = cont = 0

print('-='*15)
print('PAR OU ÍMPAR')

while True:
    comp = randint(1,10)
    print('-=' * 15)
    jogador = int(input('Digite um número: '))
    rsp = str(input('Par ou ímpar?[P/I] ')).strip().upper()
    print('-'*30)
    soma = comp + jogador
    print(f'Você digitou {jogador} e o computador {comp}. A soma é {soma}', end='')
    if soma % 2 == 0:
        print(' DEU PAR!')
        rsps = 'P'
    else:
        print(' DEU ÍMPAR!')
        rsps = 'I'
    print('-'* 30)
    if rsp == rsps:
        cont += 1
        print('VOCÊ VENCEU! PARABÉNS.')
        print('Vamos jogar novamente...')
    else:
        print('VOCÊ PERDEU! COMPUTADOR VENCEU.')
        print('-' * 30)
        break

print(f'GAME OVER! Você venceu {cont} vezes')