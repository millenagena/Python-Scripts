cont = 0
clas = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
        'Flamengo', 'Vasco da Gama','Chapecoense', 'Atlético', 'Botafogo',
        'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'Lista de times do Brasileirão:\n{clas}')
print('-='*22)
print(f'Os 5 primeiros colocados são:\n{clas[:6]}')
print('-='*22)
print(f'Os 4 últimos são:\n{clas[-4:]}')
print('-='*22)
print(f'Times em ordem alfabética:\n{sorted(clas)}')
print('-='*22)
print(f'O Chapecoense está na {clas.index("Chapecoense")}° posição')
print('-='*22)