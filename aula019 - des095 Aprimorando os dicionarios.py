dados = {}
npartidas = 0
gols = somagols = 0
golspart = []
time = []
rsp = str()

while True:
    dados.clear()
    golspart.clear()
    somagols = 0
    dados['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    npartidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for c in range(0, npartidas):
        gols = int(input(f'    Quantos gols {dados["nome"]} fez na {c+1}ª partida? '))
        somagols += gols
        golspart.append(gols)

    dados['gols por partida'] = golspart[:]
    dados['total de gols'] = somagols
    time.append(dados.copy())

    while True:
        rsp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        if rsp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if rsp == 'N':
        break

print('-='*40)
print('cod', end=' ')
for i in dados.keys():
    print(f'{i:<20}', end='')
print('-'*80)

for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-='*40)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para interromper) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' ---- LEVANTAMENTO DE DADOS DO JOGADOR {time[busca]["nome"]}: ---- ')
        for i, g in enumerate(time[busca]['gols por partida']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('FINALIZANDO...')
