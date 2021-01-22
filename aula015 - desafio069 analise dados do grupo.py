idade = m18 = mm20 = h = m = 0
sexo = rsp = ' '
while True:
        print('-='*15)
        print('Cadastre uma pessoa')
        print('-='*15)
        idade = int(input('Idade: '))
        if idade > 18:
            m18 += 1
        while sexo not in 'MF':
            sexo = str(input('Sexo[M/F]: ')).strip().upper()
            if sexo == 'F':
                m += 1
                if idade < 20:
                    mm20 += 1
            else:
                h += 1
        sexo = ' '
        print('-'*30)
        rsp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if rsp == 'N':
            break

print(f'\nTemos o total de {h+m} pessoaas cadastradas. {h} homens e {m} mulheres')
print(f'Total de pessoas com mais de 18 anos: {m18}')
print(f'Total de mulheres com menos de 20 anos: {mm20}')
