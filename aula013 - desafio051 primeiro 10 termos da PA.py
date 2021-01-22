print('='*30)
print('OS 10 PRIMEIROS TERMOS DE UMA PA')
print('='*30)

termo1 = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = termo1 + (10-1) * razao

for c in range(termo1, decimo + razao, razao):
    print(c, end=' --> ')
print('ACABOU')