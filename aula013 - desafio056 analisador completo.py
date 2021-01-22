soma = 0
hvelho = 0
nvelho = str
mmaior20 = 0
contm = 0
cont20 = 0

for p in range (1, 5):
    print(f'----- {p}° PESSOA -----')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    soma += idade
    if sexo in 'Mm' :
       if hvelho < idade:
           hvelho = idade
           nvelho = nome
    if sexo in 'Ff':
        contm += 1
        if idade > 20:
            cont20 += 1

print(f'\nA média das idades é {soma/4}')
print(f'O homem mais velho tem {hvelho} anos e se chama {nvelho}')
print(f'Ao todo tem {contm} pessoas do sexo feminino e {cont20} delas possuem mais de 20 anos')