arq = open("arquivo2.txt", "w") #criando um arquivo ja existente
arq.write("Esse é o meu arquivo")
arq.close()

arq2 = open("Meu arquivo.txt", "a") #acrescentando algo a um arquivo existente
arq2.write("\nEsse é o meu arquivo")
arq2.close()