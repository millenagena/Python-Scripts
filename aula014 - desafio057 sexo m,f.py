s = str(input('Informe seu sexo [M/F]: ')).upper()
while s != 'M' and s != 'F':
   s = str(input('Dado inválido. Informe seu sexo: ')).upper()

if s == 'M':
    print(f'\n\nSexo {s} - MASCULINO gravado com sucesso')
else:
    print(f'\n\nSexo {s} - FEMININO gravado com sucesso')