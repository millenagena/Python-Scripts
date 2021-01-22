vel = int(input('Informe a velocidade do carro em km/h: '))
if vel>80:
    multa = (vel-80)*7
    print('\nESTÁ MULTADO POR EXCESSO DE VELOCIDADE!!\n')
    print(f'Sua multa é correpondente ao valor de R${multa}')
print('\nDirija com segurança e consciência!\nTenha um bom dia.')