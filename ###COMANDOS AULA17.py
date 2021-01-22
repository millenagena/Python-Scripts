num = [2, 5, 9, 1]
print(num)

num[2] = 3
print(f'Substituindo o terceiro elemento por 3 \n{num}')

num.append(7)
print(f'Adicionando o elemento 7 \n{num}')

num.sort()
print(f'Colocando em ordem crescente \n{num}')

num.sort(reverse=True)
print(f'Colocando em ordem decrescrente \n{num}')

print(f'Essa lista tem {len(num)} elementos')

num.insert(2, 2)#Na posição dois, adicionar o elemento 2
print(f'Adicionando o elemento 2 na posição [2] \n{num}')

num.pop()
print(f'Removendo o último elemento \n{num}')

num.pop(3)
print(f'Removendo o elemento [3]-quarto elemento \n{num}')

num.remove(2)
#Nesse caso, não remove o elemento que está na posição [2], mas o elemento 2
print(f'Removendo o primeiro número 2 \n{num}')

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4 na lista\n\n\n')


valores = []
#pode ser assim tbm valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for c, v in enumerate(valores):
    print(f'Na posição {c} encoontrei o valor {v}')
print('Cheguei ao final da lista\n\n\n')

valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(valores)
for p, v in enumerate(valores):
    print(f'Na posição {p} encontrei o valor {v}')
print('\n\n\n')

a = [2, 3, 4, 7]
b = a #ligação de uma lista com a outra
b[2] = 8 #se essas listas estao ligadas, isso alterará as duas
print(f'Lista A {a}')
print(f'Lista B {b}')

c = [1, 2, 3, 4]
d = c[:] #atribui os elementos da lista c à d (copia)
d[2] = 8
print(f'Lista C {c}')
print(f'Lista D {d}')
