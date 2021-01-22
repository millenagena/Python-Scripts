'''ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')

n = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

num = int(input('Digite um número de zero a vinte: '))
while num not in n:
    num = int(input('Número inválido. Tente novamente: '))

pos = n.index(num)

print(f'\nVocê digitou o número {ext[pos]}')'''

ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')

num = int(input('Digite um número de zero a vinte: '))
while num < 0 or num > 20:
    num = int(input('Número inválido. Digite novamente: '))

print(f'Você digitou o número {ext[num]}')