pilha = []
expressao = input('Digite uma expressão numérica: ')

for simbolo in expressao:
    if simbolo == '(':
        pilha.append(simbolo)
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(simbolo)
            break
if len(pilha) == 0:
    print('\nSua expressão é válida!')
else:
    print('Sua expressão não é válida!')