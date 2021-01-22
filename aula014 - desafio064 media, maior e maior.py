rsp = 'S'
maior = menor = cont = media = soma = 0

while rsp != 'N':
    n = float(input('Digite um número: '))
    rsp = str(input('Quer continuar?[S/N] ')).strip().upper()
    if rsp == 'S':
        cont += 1
        soma += n
        if cont == 1:
            maior = menor = n
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    else:
        cont += 1
        soma += n
        print('Finalizando...')
media = soma/cont
print(f'\n\nVocê digitou {cont} números. A soma deles é {soma:.2f}. A média deles é {media:.2f}')
print(f'O maior deles é {maior} e o menor deles é {menor}')