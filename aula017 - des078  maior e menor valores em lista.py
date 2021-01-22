numeros = []
maior = menor = 0

for n in range(0, 5):
    numeros.append(int(input('Digite um valor: ')))

print('\nOs números digitados foram: ')

for p, num in enumerate(numeros):
    print(num, end=' ')
    if p == 0:
        maior = num
        menor = num
    if maior < num:
        maior = num
    if menor > num:
        menor = num

print(f'\n\nO menor número é {menor} nas posições', end=' ')
for i, v in enumerate(numeros):
    if v == menor:
        print(i+1, end=' ')
print(f'\nO maior número é {maior} nas posições', end=' ')
for i, v in enumerate(numeros):
    if v == maior:
        print(i+1, end=' ')
