from datetime import date

anonas = int(input('Informe o ano de nascimento: '))
anoatual = date.today().year
idade = anoatual-anonas
print(f'O atleta tem {idade} anos.')

if idade<=9:
    print('\nO atleta é classificado como MIRIM!')
elif idade>9 and idade<=14:
    print('\nO atleta é classificado como INFANTIL!')
elif idade>14 and idade<=19:
    print('\nO atleta é classificado como JUNIOR!')
elif idade>19 and idade<=25:
    print('\nO atleta é classificado como SÊNIOR!')
else:
    print('\nO atleta é classificado como MASTER!')