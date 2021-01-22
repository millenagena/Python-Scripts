a = input('Type something: ')

print('The primitive type of this value is: {}'.format(type(a)))

print('Does it have only numbers? {}'.format(a.isnumeric()))
print('Does it have only letters? {}'.format(a.isalpha()))
print('Does it have only numbers and letters? {}'.format(a.isalnum()))
print('Does it have only spaces? {}'.format(a.isspace()))
print('Is it in capital letters? {}'.format(a.isupper()))
print('Is it in lowercase? {}'.format(a.islower()))
print(f'Is it capitalized? {a.istitle()}')
