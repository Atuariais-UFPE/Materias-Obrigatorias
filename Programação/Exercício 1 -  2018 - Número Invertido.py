###Número Invertido###
x = int(input("Digite um número inteiro de três algarismos: "))
c = (x%10)*100
d = (x//10%10)*10
u = (x//100)
if x < 100 or x > 999:
    print("Valor inválido")
else:
    print ("Seu número invertido é: " ,c+d+u)
