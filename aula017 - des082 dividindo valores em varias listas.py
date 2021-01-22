lista = []
pares = []
impares = []
'''while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    rsp = str(input('Quer continuaar?[S/N] ')).strip()
    if rsp not in 'Ss':
        break'''

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    rsp = str(input('Quer continuar?[S/N] ')).strip()
    if rsp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)


print('-='*30)
print(f'A lista de números digitados completa é {lista}')
print(f'A lista de números pares digitados é {pares}')
print(f'A lista de números ímpares digitados é {impares}')