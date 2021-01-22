'''from math import sqrt
CO = float(input('Qual o comprimento do cateto oposto: '))
CA = float(input('Qual o comprimento do cateto adjacente: '))
H = sqrt((CO**2) + (CA**2))
print('O comprimento da hipotenusa é: {:.2f}'.format(H))'''

from math import hypot
CO = float(input('Comprimento do cateto oposto: '))
CA = float(input('Comprimento do cateto adjacente: '))
H = hypot(CO, CA)
print(f'O comprimento da hipotenusa é: {H:.2f}')