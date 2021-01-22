v1 = int(input('Informe o primeiro valor: '))
razao = int(input('Informe a razão: '))
n = 1

while n <= 10:
    print(f'{v1} --> ', end='')
    v1 = v1 + razao
    n += 1
print('FIM')