n = int(input('Digite a quantidade de termos da sequência de fibonacci: '))
cont = 2
p = 0
s = 1
print('0  1', end=' ')
while cont <= n:
    t = p + s
    print(f' {t}', end=' ')
    p = s
    s = t
    t = 0
    cont += 1
print('\nFIM.')