'''numeros = []
rsp = ' '
i = 0
while True:
        numeros.append(int(input('Digite um valor: ')))
        if i != 0:
            for n in range(0, len(numeros)):
                if i != n:
                    if numeros[i] == numeros[n]:
                        numeros.pop()
                        print('Esse número já foi adicionado!')
                    else:
                        print('Número adicionado com sucesso...')
        elif i == 0:
            print('Número adicionado com sucesso...')
        rsp = str(input('Quer continuar?[S/N] ')).strip().upper()
        if rsp in 'Nn':
            break
        else:
            i += 1
print(numeros)'''

numeros = list()

while True:
    n  = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    rsp = str(input('Quer continuar?[S/N] ')).strip()
    if rsp in 'Nn':
        break
print('Os números digitados foram {}'.format(numeros))