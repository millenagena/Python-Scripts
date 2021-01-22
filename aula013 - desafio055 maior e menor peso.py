for p in range (1, 6):
    peso = float(input(f'Informe o peso da {p}° pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso

print(f'\nO maior peso é {maior:.2f} kg')
print(f'O menor peso é {menor:.2f} kg')