num = str(input('Informe um número inteiro de dois dígitos: '))
if num[0]>num[1]:
    print('O primeiro dígito é maior!')
elif num[0]==num[1]:
    print('O primeiro dígito é igual ao segundo!')
else:
    print('O segundo dígito é maior!')