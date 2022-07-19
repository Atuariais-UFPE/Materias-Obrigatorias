###Círculo###
print ("Vamos verificar se um determinado ponto se encontra dentro da área de um círculo")
a = float(input("Defina uma coordenada X para o centro do círculo: "))
b = float(input("Defina uma coordenada Y para o centro do círculo: "))
r = float(input("Digite o raio do círculo:" ))
print("Vamos verificar  onde se localiza um ponto em relação à um círculo de raio 5")
x = float(input("Digite uma coordenada X para o ponto: "))
y = float(input("Digite uma coordenada Y para o ponto: "))
if (x-a)**2 + (y-b)**2 == r**2:
    print ("O ponto está sobre o raio do círculo")
elif (x-a)**2 + (y-b)**2 < r**2:
    print ("O ponto está no interior do círculo")
elif (x-a)**2 + (y-b)**2 > r**2:
    print ("O ponto está fora do círculo")
else:
    print ("Valores não suportados")
