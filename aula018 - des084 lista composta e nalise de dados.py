dados = []
pessoal = []
rsp = ' '
cont = maiorp = menorp = 0
nmaior = []
nmenor = []

while True:
    dados.append(str(input('\nNome: ')))
    dados.append(float(input('Peso: ')))
    cont += 1
    if cont == 1:
        maiorp = dados[1]
        nmaior.append(dados[0])
        menorp = dados[1]
        nmenor.append(dados[0])
    else:
        if dados[1] > maiorp:
            maiorp = dados[1]
            nmaior.clear()
            nmaior.append(dados[0])
        elif dados[1] == maiorp:
            nmaior.append(dados[0])
        if dados[1] < menorp:
            menorp = dados[1]
            nmenor.clear()
            nmenor.append(dados[0])
        elif dados[1] == menorp:
            nmenor.append(dados[0])
    pessoal.append(dados[:])
    dados.clear()
    rsp = input('Quer continuar?[S/N] ').strip()
    if rsp not in 'Ss':
        break
print('-='*30)
print(f'Ao todo foram cadastradas {cont} pessoas: ', end='')

for p in pessoal:
    print(f'{p[0]}', end=' ')

print(f'\nAs pessoas mais pesadas são {nmaior} com {maiorp:.2f} kg')
print(f'As pessoas mais leves são {nmenor} com {menorp:.2f} kg')

#Para mostrar as pessoas mais pesadas e mais leves também tem a seguinte opção:
#Após encontrar o maior peso no laço basta exibir os nomes por um for:
'''print('As pessoas mais pesadas são: ')
for p in pessoal:
    if p[1] == maiorp:
        print(f'{p[0]}')'''