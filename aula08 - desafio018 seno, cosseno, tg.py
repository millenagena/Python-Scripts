from math import radians, sin, cos, tan
ang = float(input('Informe o ângulo: '))
angrad = radians(ang)
sin = sin(angrad)
cos = cos(angrad)
tan = tan(angrad)

print(f'O ângulo {ang:.2f}° em rad. é {angrad:.2f}')
print(f'O SENO desse ang.: {sin:.2f}')
print(f'O COSSENO desse ang.: {cos:.2f}')
print(f'A TANGENTE desse ang.: {tan:.2f}')
