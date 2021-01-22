peso = float(input('Informe seu peso em kg: '))
altura = float(input('Informe sua altura: '))
#calculando IMC
imc = peso/(altura*altura)

if imc<18.5:
    print('Você está ABAIXO DO PESO NORMAL!')
elif imc>=18.5 and imc<25:
    print('Você está no PESO IDEAL!')
elif imc>=25 and imc<30:
    print('Você está SOBREPESO!')
elif imc>=30 and imc<40:
    print('Você está OBESO! Cuidado.')
elif imc>=40:
    print('Você está com OBESIDADE MÓRBIDA! Cuide-se.')