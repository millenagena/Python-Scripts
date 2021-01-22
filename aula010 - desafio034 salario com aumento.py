salario = float(input('Informe o valor do seu salário: '))
if salario<= 1250.00:
    novo = (15/100*salario) + salario
else:
    novo = (10/100*salario) + salario
print(f'O valor do seu salário com o aumento é R${novo:.2f}')
