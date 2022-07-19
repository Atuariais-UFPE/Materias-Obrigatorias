###Lista de Fatoriais###
n = int(input("Digite um número: "))
lista = []
cont = 1
fat = 1
while cont <= n:
    fat = fat*cont
    cont += 1
    lista.append(fat)
print(lista)
