s1 = float(input('Informe a medida do primeiro segmento: '))
s2 = float(input('Informe a medida do segundo segmento: '))
s3 = float(input('Informe a medida do terceiro segmento: '))
#Cada um desses segmentos tem que ser menor que a soma dos outros dois
if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('Esses segmentos formam um triângulo: \n')
    if s1 == s2 and s2 == s3:
        print('EQUILÁTERO!')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('\nEsses segmentos não formam um triângulo.')