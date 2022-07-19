###Raiz Cúbica###
x = int(input("Digite um número inteiro: "))
if x < 0:
    raiz = x
else:
    raiz = 1
while raiz*raiz*raiz < x:
    raiz += 1
if raiz*raiz*raiz == x:
    print("A raiz de", x, "é", raiz)
else:
    print("O número", x, "não tem raiz") 
    
