p = float(input('Informe o preço do produto: '))
por = 5/100*p
liq = p - por

print(f'O preço do produto com 5% de desconto é: R${liq:.2f}')