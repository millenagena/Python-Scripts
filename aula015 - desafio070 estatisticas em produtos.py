prod = rsp = nmenor = ' '
preco = menor = cont = mmil = soma = 0
print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
while True:
        prod = str(input('Nome do produto: '))
        cont += 1
        preco = float(input('Preço: R$ '))
        soma += preco
        if cont == 1:
            menor = preco
            nmenor = prod
        if menor > preco:
            menor = preco
            nmenor = prod
        if preco > 1000:
            mmil += 1
        rsp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if rsp == 'N':
            break

print(f'\nO total da compra foi de R${soma:.2f}')
print(f'Ao todo foram comprados {mmil} produtos que custam mais de mil reais')
print(f'O produto mais barato comprado foi {nmenor} que custou R${menor:.2f}')