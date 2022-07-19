###Fatorial de um Número###
x = int(input("Digite um número inteiro positvo: "))
fat = x
if x == 1 or x == 0:
    fat = 1
else:
    while x > 2:
        fat = x(x-1)
        x -=1
print("O fatorial de", x, "é", fat)
