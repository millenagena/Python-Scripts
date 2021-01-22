somapar = 0
cont = 0

for c in range (1,7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num%2 == 0:
        cont = cont + 1
        somapar = somapar + num

print('\nA soma dos {} números pares informados é {}'.format(cont, somapar))