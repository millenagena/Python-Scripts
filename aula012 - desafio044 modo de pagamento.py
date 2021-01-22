valor = float(input('Qual o valor das compras? '))
mpag = int(input("""Qual o modo de pagamento?\n
[1] Á vista (dinheiro/cheque)
[2] Á vista (cartão)
[3] 2x no cartão
[4] 3x ou mais no cartão\n """))

if mpag == 1:
    valorn = valor - (10/100*valor)
    print(f'O valor total a ser pago é: R${valorn:.2f}')
elif mpag == 2:
    valorn = valor - (5/100*valor)
    print(f'O valor total a ser pago é: R${valorn:.2f}')
elif mpag == 3:
    valorn = valor
    print(f'O valor total a ser pago é: R${valorn:.2f}')
    print(f'Dividido em 2 parcelas de {valorn/2:.2f}')
elif mpag == 4:
    valorn = valor + (20/100*valor)
    parcelas = int(input('Em quantas parcelas? '))
    mensal = valorn/parcelas
    print(f'O valor total a ser pago é R${valorn}')
    print(f'Dividido em {parcelas} parcelas no valor de R${mensal:.2f}')

