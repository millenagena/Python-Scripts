numeros = []
for c in range (0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or c > numeros[-1]:
        numeros.append(n)
        print('Número adicionado na última posição da lista')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Número adicionado na posição {pos} da lista')
                break
            pos +=1
print(f'Os números digitados em ordem crescente {numeros}')