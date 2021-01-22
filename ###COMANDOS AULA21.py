def linha():
    print('-='*20)


def fatorial(n = 1): #Parametro opcional(caso nao seja passado valor pra n ele vale 1)
    f = 1
    for c in range(n, 0, -1):
        f = f * c
    return f


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


#Programa Principal
num = int(input('Digite um número: '))
print(f'O fatorial do número {num} é {fatorial(num)}')
linha()
f1 = fatorial(4)
f2 = fatorial(5)
f3 = fatorial()
print(f'Os resultados dos fatoriais de 4, 5 e nada são {f1}, {f2} e {f3}')
linha()
rsp = int(input('Digite um número para analisarmos se é par ou não: '))
print(f'{par(rsp)}')
if par(rsp):
    print('É par!')
else:
    print('Não é par!')
