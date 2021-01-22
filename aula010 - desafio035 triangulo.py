s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
#Cada um desse segmentos tem que ser menor que a soma dos outros dois
if s1 < s2+s3 and s2 < s1+s3 and s3 < s1+s2:
    print('Esses segmentos podem formar um triângulo')
else:
    print('Esses segmentos não podem formar um triângulo')
