dados = []
rsp = ' '
while True:
    nome = str(input('Nome: ')).strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    dados.append([nome, [n1, n2], media])
    rsp = str(input('Quer continuar?[S/N] ')).strip()
    if rsp not in 'Ss':
        break
print('-='*30)
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*26)
    opc = int(input('Mostrar as notas de qual aluno (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
    elif opc <= len(dados):
        print(f'As notas de {dados[opc][0]} são {dados[opc][1]}')