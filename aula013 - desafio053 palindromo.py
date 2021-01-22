frase = str(input('Informe uma palavra/frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('Você digitou a frase {}'.format(frase))

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(f'A frase {junto} invertida é {inverso}\n')
print('Sendo assim...')
if inverso == junto:
    print('\nTemos um palíndromo!')
else:
    print('\nA frase não é um palíndromo!')
