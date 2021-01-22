from random import randint

comp = randint(0, 10)
print('''Sou seu computador...
      Acabei de pensar em um número entre 0 e 10.
      Você consegue adivinhar qual é?''')
n = int(input('\nQual seu palpilte? '))
cont = 1

while n != comp:
    if n > comp:
        print('\nMenos... Tente mais uma vez!')
        n = int(input('Qual seu palpite? '))
        cont += 1
    elif n < comp:
        print('\nMais... Tente mais uma vez!')
        n = int(input('Qual seu palpite? '))
        cont += 1
if cont == 1:
    print('\nPARABÉNS! Você acertou de primeira. <3')

print(f'\n\nAcertou depois de {cont} tentativas. Parabéns!')