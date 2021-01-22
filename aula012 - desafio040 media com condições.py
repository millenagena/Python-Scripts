n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))
media = (n1+n2)/2
print(f'A média desse aluno é {media}')
if media<5.0:
    print('\nO aluno foi \033[31mREPROVADO!\033[m')
elif media>=5.0 and media<6.9:
    print('\nO aluno está de \033[31mRECUPERAÇÃO!\033[m')
else:
    print('\nO aluno está \033[36mAPROVADO!\033[m')