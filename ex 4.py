def ler_arquivo(a):
    a1 = open(a)
    linhas = a1.readlines()
    for l in linhas:
        print(f'{l}')


def fechar(a2):
    a2.close()


while True:
    print('Manipulando arquivos')
    print('\nEscolha a opção desejada: ')
    op = input('1 - Abrir e ler um arquivo \n2 - Ler novamente\n3 - Fechar o arquivo\n')

    if op == '1':
        arq = input('Digite o nome do arquivo que deseja ler: ')
        ler_arquivo(arq)
    elif op == '2':
        ler_arquivo(arq)
    elif op == '3':
        fechar(arq)
        break
    else:
        print('Opção inválida')
