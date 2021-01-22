palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis',
            'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')
vogais = ('A', 'E', 'I', 'O', 'U')

for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')