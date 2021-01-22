'''teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = []
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
print(teste)
galera.append(teste[:])
print(galera)'''

'''galera1 = [['João', 15], ['Maria', 22], ['Lúcia', 18]]
print(galera1)
print('\n')
for p in galera1:
    print(f'{p[0]} tem {p[1]} anos de idade')'''

galera2 = []
dados = []

for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera2.append(dados[:])
    dados.clear()
print(galera2)

for p in galera2:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} não é maior de idade')