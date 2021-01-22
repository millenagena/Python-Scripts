primeiro = int(input('Primeiro valor: '))
razao = int(input('Razão: '))
n = 1
op = 1
cont = 10
termo = primeiro
c = 1

while op != 0:
    while n <= 10:
        print(f'{termo} --> ', end='')
        termo += razao
        n += 1
    print('PAUSA')
    op = int(input('\nQuantos termos a mais você deseja? '))
    cont += op

    while c <= op:
        print(f'{termo} --> ', end='')
        termo += razao
        c += 1
    c = 1
    if op == 0:
        print('\nFinalizando...')

print(f'Progressão aritmética finalizada com {cont} termos')
