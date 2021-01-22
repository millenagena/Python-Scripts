n = 0
mult = 0
print('FABRICADOR DE TABUADA')
print('-='*22)
while True:
    n = int(input('Qual tabuada quer saber? '))
    print('-'*22)
    if n < 0:
        break
    while mult <= 10:
        print(f'{n} x {mult} = {n*mult}')
        mult += 1
    mult = 0
    print('-'*22)
print('PROGRAMA TABUADA ENCERRADO.')