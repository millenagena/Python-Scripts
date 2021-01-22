nome = input('Digite o nome do arquivo que deseja abrir: ').strip()
arq = open(nome)
print(f'{arq.read()}')
arq.close()
