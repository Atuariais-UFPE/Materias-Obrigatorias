###Lista de Primos###
num = int(input("Digite um número: "))
lista = []
cont1 = 2
while cont1 <= num:
    cont2 = 2
    primo = True
    while cont2 < cont1 and primo == True:
        if cont1 % cont2 == 0:
            primo = False
        cont2 += 1
    if primo == True:
        lista.append(cont1)
    cont1 += 1
print(lista)
    
    
