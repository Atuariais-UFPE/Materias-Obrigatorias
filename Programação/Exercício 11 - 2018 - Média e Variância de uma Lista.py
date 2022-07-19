###Média é Variância de uma Lista###
lista = []
continua = True
cont = -1
soma1 = 0
soma2 = 0
while continua == True:
    n = float(input("Digite um número: "))
    if n >= 0:
        lista.append(n)
        cont += 1
    else:
        continua = False
termos = cont + 1
while cont >= 0:
    soma1 += lista[cont]
    soma2 += (lista[cont])**2
    cont -= 1
média = soma1/termos
var = (soma2/termos) - média
print("A média é igual a", média)
print("A variância é igual a", var)
                    
