'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print()
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
for k in pessoas.keys():
    print(k)
print()
for v in pessoas.values():
    print(v)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98
print(pessoas)'''

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print()
print(estado1)
print(estado2)
print(brasil)
print()
print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
print()
for e in brasil:
    print(e)
print()
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem o valor {v}')
print()

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()