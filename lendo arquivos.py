arquivo = open("meu arquivo.txt")

linhas = arquivo.readlines() #salva cada linha do arquivo em uma lista
print(linhas)

for linha in linhas: #apresenta uma linha de cada vez
	print(linha).strip()

texto_completo = arquivo.read() #salva o arquivo todo em uma variavel so para apresentar na tela
print(texto_completo)

