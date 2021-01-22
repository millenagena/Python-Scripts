l = float(input('Informe a largura da parede: '))
h = float(input('Informe a altura da parede: '))
a = float(l*h)
t = a/2
print(f'A área dessa parede é: {a:.2f}m²')
print(f'Considerando que 1l de tinta pinte 1m²')
print(f'Concluimos que serão necessários {t:.2f} litros para pintar essa parede de {a:.2f}m²')
