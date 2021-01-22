print('Os números ímpares e múltiplos de 3 do intervalo de 1 à 500 são:\n ')
n = 0
soma = 0

for c in range (1, 500+1, 2):
    if c%3==0:
        print(c, end=' ')
        n = n + 1
        soma = soma + c

print('\n\nA soma resultante desses {} números é: {}'.format(n, soma))
