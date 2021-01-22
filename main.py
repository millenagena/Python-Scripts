import aleatorio as a
import media as m

lista = a.geralista(4)
media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print('Minha lista eh: {}'.format(lista))
print('A media da minha lista eh: {}'.format(media))
print('A mediana da minha lista eh: {}'.format(mediana))
