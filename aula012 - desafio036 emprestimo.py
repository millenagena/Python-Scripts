vc = float(input('Qual o valor da casa? '))
sal = float(input('Qual o valor do seu salário? '))
anos = float(input('Em quantos anos ira pagar?'))

nparcelas = 12*anos
vparcelas = vc/nparcelas
print('O valor de cada prestação mensal será de R${:.2f}'.format(vparcelas))
porcent = 30/100*sal

if vparcelas>porcent:
    print('\nO valor da parcela excede os 30% se seu salário mensal.\n\033[0;31mEMPRÉSTIMO NEGADO!!\033[m')
else:
    print('\n\033[4;32mEMPRÉSTIMO CONCEDIDO!!\033[m')