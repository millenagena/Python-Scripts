op = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while op != 5:
    print('-'*15)
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    op = int(input('\nEscolha sua opção: '))
    print('-'*15)
    if op == 1:
        print(f'SOMA: {n1} + {n2} = {n1+n2}')
    elif op == 2:
        print(f'MULTIPLICAÇÃO: {n1} x {n2} = {n1*n2}')
    elif op == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que {n2}')
        elif n1 == n2:
            print(f'Os números digitados são iguais')
        else:
            print(f'O número {n2} é maior que {n1}')
    elif op == 4:
        print('\nInforme os novos valores...\n')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op < 1 or op > 5:
        print('OPÇÃO INVÁLIDA! Tente novamente')

if op == 5:
    print('\nObrigada por utilizar o programa. Tenha um bom dia!')