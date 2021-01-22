dados = {}
npartidas = 0
gols = somagols = 0
golspart = []

dados['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
npartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

for c in range(0, npartidas):
    gols = int(input(f'Quantos gols {dados["nome"]} fez na {c+1}ª partida? '))
    somagols += gols
    golspart.append(gols)
dados['gols por partida'] = golspart[: ]
dados['total de gols'] = somagols

print('-='*30)
print(dados)
print('-='*30)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {dados["nome"]} jogou {npartidas} partidas')
for i, g in enumerate(golspart):
    print(f'    => Na partida {i+1} fez {g} gols')
print(f'O total de {somagols} gols')




