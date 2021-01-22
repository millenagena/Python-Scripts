
listagem = ('Lápis', 1.75,
            'Caderno', 15.70,
            'Borracha', 2,
            'Estojo', 12,
            'Régua', 1.25,
            'Compasso', 5,
            'Mochila', 150)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'{listagem[pos]:>7.2f}')
print('-'*40)