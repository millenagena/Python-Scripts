from datetime import date
cadastro = {}
anoaposentadoria = nasc = 0

cadastro['nome'] = str(input('Nome: ')).strip().capitalize()
nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc
cadastro['idade'] = idade
cadastro['CTPS'] = int(input('Número carteira de trabalho(0 se não tem): '))

if cadastro['CTPS'] != 0:
    cadastro['ano de contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário (R$): '))
    anoaposentadoria = cadastro['ano de contratação'] + 35
    cadastro['aposentadoria'] = anoaposentadoria - nasc
print('-='*30)

for k, v in cadastro.items():
    print(f'- {k} tem o valor {v}')