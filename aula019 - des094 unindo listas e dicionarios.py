pessoa = {}
galera = []
rsp = str()
somaidade = media = qntdp =  0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        rsp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if rsp in 'SN':
            break
        else:
            print('ERRO! Digite apenas S ou N')
    if rsp in 'Nn':
        break
print('-='*30)
print(f'A) Ao todo foram cadastradas {len(galera)} pessoas.')
media = somaidade/len(galera)
print(f'B) A média das idades é {media}')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('D) As pessoas com idade acima da média são ', end='')
for p in galera:
    if p['idade'] > media:
        print(f'    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
print('-='*30)
print('<<< ENCERRADO >>>')