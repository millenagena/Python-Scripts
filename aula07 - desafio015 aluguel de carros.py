d = float(input('Quantos dias o carro foi utilizado? '))
km = float(input('Quantos km foram percorridos? '))

qntdd = 60*d
qntdkm = 0.15*km
total = qntdd+qntdkm

print('O total a ser pago é de: {}'.format(total))