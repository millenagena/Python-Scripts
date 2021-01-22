num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Os números digitados foram {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro valor 3 foi digitado na posição {num.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os números pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
