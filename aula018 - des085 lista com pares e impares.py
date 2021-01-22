numeros = [[], []]
num = 0
for n in range (0, 7):
    num = int(input(f'Digite o {n+1} valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print('-='*30)
print(f'Os números digitados foram {numeros}')
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares digitados foram {numeros[0]}')
print(f'Os números ímpares digitados foram {numeros[1]}')
