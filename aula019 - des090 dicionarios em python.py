alunos = {}
sit = ' '
alunos['nome'] = str(input('Nome: '))
alunos['média'] = float(input('Média: '))

if alunos['média'] >= 7:
    alunos['situação'] = 'Aprovado'
elif alunos['média'] < 7:
    alunos['situação'] = 'Reprovado'
print(alunos)

for k, v in alunos.items():
    print(f'O {k} é igual a {v}')
