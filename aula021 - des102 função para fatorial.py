def fatorial(n, show = False):
    """
    --> Calcula o fatorial de um número
    :param n: número a ser calculado o fatorial
    :param show: valor lógico se deseja ou não aparesentar a conta
    :return: retorna a função principal o resultado do fatorial
    """
    fat = 1
    if show == False:
        for c in range(n, 0, -1):
            fat *= c
    elif show == True:
        for c in range(n, 0, -1):
            fat *= c
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    return fat


#Programa principal
print('-'*60)
num = int(input('Digite um número para calcular o fatorial: '))
rsp = str(input('Deseja ver a conta?[S/N] ')).strip()[0]
print('-'*60)
if rsp in 'Ss':
    print(fatorial(num, show = True))
else:
    print(fatorial(num, show = False))

help(fatorial)