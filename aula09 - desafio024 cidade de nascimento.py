"""c = str(input('Informe a cidade que você nasceu: ')).strip()
cma = c.upper()
print(cma[:5]=='SANTO')"""


c = str(input('Informe a cidade que você nasceu: ')).strip()
cma = c.upper()
lista = cma.split()
answer = 'SANTO' in lista[0]
print(answer)
