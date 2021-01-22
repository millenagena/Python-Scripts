#concatena listas

lista1 = [1,2,3,4,5]
lista2 = ['a','b','c','d','e']
lista3 = [2,4,6,8,10]

for indice, nome, valor in zip(lista1, lista2, lista3):
    print(indice, nome, valor)