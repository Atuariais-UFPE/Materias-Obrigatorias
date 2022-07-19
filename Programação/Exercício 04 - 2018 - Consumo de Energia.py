###Consumo de Energia###
print("Vamos calcular o consumo de energia")
d = str(1)
c = str(2)
i = str(3)
x = str(input("Qual o tipo de instalação? Digite (1) para doméstica, (2) para comercial e (3) industrial: "))
y = float(input("Qual foi o consumo de energia em Kwh?: "))
if x == d and y <= 500:
    print("O valor da conta é R$", y * 0.40)
elif x == d and y > 500:
    print("O valor da conta é R$", y * 0.65)
elif x == c and y <= 1000:
    print("O valor da conta é R$", y * 0.55)
elif x == c and y > 1000:
    print("O valor da conta é R$", y * 0.60)
elif x == i and y <= 5000:
    print("O valor da conta é R$", y * 0.50)
elif x == i and y > 5000:
    print("O valor da conta é R$", y * 0.60)
else:
    print("Valores digitados não suportados")
        
    
