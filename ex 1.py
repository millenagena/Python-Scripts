import re

w1 = input("Digite a primeira sequência: ")
w2 = input("Digite a segunda sequência: ")
'''if w1 == w2:
    print("Sequências iguais")
else:
    print("Sequências diferentes")'''

#Utilizando expressões regulares

busca = re.match(w1,w2)
if busca:
    print("Sequências iguais")
    print(busca.group())
else:
    print("Sequências diferentes")