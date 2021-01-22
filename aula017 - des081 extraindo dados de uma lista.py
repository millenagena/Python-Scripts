lista = []
cont = 0
rsp = ' '
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    cont += 1
    rsp = str(input('Quer continuar?[S/N] ')).strip()
    if rsp not in 'Ss':
        break

lista.sort(reverse=True)
print(f'\nVocê digitou {cont} elementos')
print('A ordem decrescente desses elementos é {}'.format(lista))
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')