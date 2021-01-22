from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual-ano
print(f'Quem nasceu em {ano} tem {idade} anos em {anoatual}')

if idade<18:
    print('\n\033[36mVocê ainda não está na idade de se alistar!')
    anoalista = ano+18
    print(f'Você deve se alistar no ano de {anoalista}.\033[m')
elif idade==18:
    print('\n\033[32mVocê deve alistar-se nesse ano!\033[m')
else:
    print('\n\033[31mVocê já passou da idade de se alistar!')
    anoalista = ano+18
    print(f'Você deveria ter se alistado no ano de {anoalista}.\033[m')
