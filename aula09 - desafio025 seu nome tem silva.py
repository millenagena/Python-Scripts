nome = str(input('Digite seu nome completo: ')).strip()
nomema = nome.upper()
answer = 'SILVA' in nomema[:]
print(f'Seu nome tem Silva?! {answer}')

"""nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome[:].lower()))"""


