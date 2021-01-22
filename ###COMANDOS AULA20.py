def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A + B = {s}')
    print()


def contador(* num): #Tuplas empacotada (recebendo diversos valores)
    tam = len(num)
    print(f'Recebi os valores {num} e ao todo são {tam} números')
    for valor in num: #Desempacotando
        print(valor, end=' ')
    print('FIM!')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


#Programa Principal
soma(4, 5)
soma(a = 4, b = 9)
soma(b = 2, a = 1)

'''a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)'''

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print()

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
