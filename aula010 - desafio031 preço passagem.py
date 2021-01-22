km = float(input('Informe a distância de sua viagem: '))
print(f'Você realizará uma viagem de {km}km')
if km<=200:
    preco = km*0.50
    print(f'\nO preço da sua passagem é: R${preco:.2f}')
else:
    preco2 = km*0.45
    print(f'\nO preço da sua passagem é: R${preco2:.2f}')
print('Have a nice trip!!')