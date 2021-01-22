matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3c = mav2 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Termo[{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar = somapar + matriz[l][c]
        if c == 2:
            soma3c = soma3c + matriz[l][c]
        if l == 1 and c ==0:
            mav2 = matriz[l][c]
        elif l == 1:
            if matriz[l][c] > mav2:
                mav2 = matriz[l][c]
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('-='*30)
print(f'A soma dos valores da terceira coluna é {soma3c}')
print(f'O maior valor da segunda linha é {mav2}')
print(f'A soma dos valores pares é {somapar}')


'''Outro modo de fazer era fazendo um "for" que percoresse somente as colunas com uma linha
fixa para descobrir o maior valor da linha 2
e contruir um "for" com coluna fixa para somar todos os valores da coluna 3

for l in range (0, 3):
    soma3c += matriz[l][2]
    
for c in range(0, 3):
    if c == 0:
        mav2 = matriz[1][c]
    elif matriz[1][c] > mav2:
        mav2 = matriz[l][c]'''