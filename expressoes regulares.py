import re
import requests

stringteste = 'O gato é bonito'
padrao = re.search(r'gat\w', stringteste) # o search encontra somente uma vez o padrao desejado, nao percorrendo a string inteira
if padrao:
	print(padrao.group()) # pra apresentar o padrao e nao o objeto
else:
	print('Padrao nao encontrado')

# Regular expressions 101
# r: RAW string (string pura) - considera por exemplo os "\n" como parte da sring
# \w significa que deve ter mais um caractere no local informado (letras ou números)
# \w+ siginifica que deve ter 1 caractere ou mais (letras ou números)
# . serve para indicar a presença de qualquer caractere (incluindo espaços)
# \w* repete o padrao por zero ou infinita vezes
# [gat]: a utilização de colchetes indica que esta sendo procurada uma letra por vez g, a ou t (no exemplo)

stringteste2 = '\nsdbasi-sdds@dasda.com\nds@sds.com\nsudbasudasu'
padrao2 = re.findall('[\w\.-]+@[\w-]+\.[\w-]+', stringteste2) #o findall percorre a string inteira, formando uma lista com todos os padroes encontrados
if padrao2:
	print(padrao2)
else:
	print('Padrao nao encontrado')
# o padrao acima eh utilizado para identificar emails

requisicao = requests.get
