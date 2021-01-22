from datetime import date
anoatual = date.today().year
cont = 0
contagr = 0
contma = 0

for n in range (0,7):
    ano = int(input(f'Informe o ano de nascimento da {n+1}° pessoa: '))
    if anoatual - ano < 18:
        cont += 1
    elif anoatual - ano == 18:
        contagr += 1
    else:
        contma += 1

print(f'\n{cont} pessoas ainda não atingiram a maioridade.')
print(f'{contagr} pessoas atingiram ou atingirão a maioridade esse ano.')
print(f'{contma} pessoas já atingiram a maioridade.')
