###Lista de Palavras de uma String###
def Lista_Palavras(string):
    listastrings = []
    stringaux = " .,;:!?-"
    palavra = str()
    for caractere in string:
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
                
                
        
