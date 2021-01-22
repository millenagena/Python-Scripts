def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.2f}x{c:.2f} é de {a:.2f} m².')

print('-='*15)
print(f'{"Controle de Área":^30}')
print('-='*15)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
