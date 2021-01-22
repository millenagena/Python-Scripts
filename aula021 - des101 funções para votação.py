
def voto(a):
    from datetime import date
    id = date.today().year - a
    if id < 16:
        return f'Com idade {id} anos: voto NEGADO!'
    elif id >= 16 and id < 18 or id >= 65:
        return f'Com idade {id} anos: voto OPCIONAL!'
    else:
        return f'Com idade {id} anos: voto OBRIGATÓRIO!'

#Programa principal
anonas = int(input('Informe seu ano de nascimento: '))
print(voto(anonas))
