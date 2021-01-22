n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um valor (999 para parar): '))
    if n != 999:
        cont += 1
        soma = soma + n
    else:
        print('Finalizando...')
print(f'\nVocê digitou {cont} números, e a soma deles resulta em {soma}')