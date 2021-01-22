'''c100 = c50 = c20 = c10 = c5 = c2 = 0
v = int(input('Qual valor você quer sacar? '))

c100 = v//100
c50 = (v%100)//50
c20 = ((v%100)%50)//20
c10 = (((v%100)%50)%20)//10
c5 = ((((v%100)%50)%20)%10)//5
c2 = (((((v%100)%50)%20)%10)%5)//2

if c100 != 0:
    print(f'{c100} cédulas de R$ 100.00')
if c50 != 0:
    print(f'{c50} cédulas de R$ 50.00')
if c20 != 0:
    print(f'{c20} cédulas de R$ 20.00')
if c10 != 0:
    print(f'{c10} cédulas de R$ 10.00')
if c5 != 0:
    print(f'{c5} cédulas de R$ 5.00')
if c2 != 0:
    print(f'{c2} cédulas de R$ 2.00')'''

valor = int(input('Qual  valor você quer sacar? '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} notas de {ced} reais')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break








