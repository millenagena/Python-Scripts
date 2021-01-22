def listastring(lista):
    string = ''

    for i in range(len(lista)-1):
        string += str(lista[i] + ', ')
    string += str('and ' + lista[len(lista)-1])
    print(string)

#main
spam = ['apples', 'bananas', 'tofu', 'cats']
listastring(spam)