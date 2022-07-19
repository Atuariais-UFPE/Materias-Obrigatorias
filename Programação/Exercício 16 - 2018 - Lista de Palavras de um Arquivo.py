###Lista de Palavras de um Arquivo###
def Lista_Palavras(string):
    arq = open("string", "r")
    lista = arq.realines()
    arq.colse()
    listastrings = []
    stringaux = " .,;:!?-\n"
    palavra = str()
    for caractere in lista:
        add = True
        for pontuação in stringaux:
            if caractere == pontuação:
                add = False
        if add == True:
            palavra += caractere
        elif palavra == str():
            pass
        else:
            listastrings.append(palavra)
            palavra = str()
    return listastrings


