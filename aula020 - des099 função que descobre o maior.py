from time import sleep

def maiorvalor(* num):
    tam = len(num)
    maior = cont = 0
    print('-='*20)
    print(f'Ao todo foram passados {tam} valores: ')
    for v in num:
        print(v, end=' ')
        sleep(0.5)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'\nE o maior desses valores é {maior}')
    print('-='*20)


#Programa principal
maiorvalor(2, 3, 9, 4, 6)
maiorvalor(4, 7, 0)
maiorvalor(6)
maiorvalor()