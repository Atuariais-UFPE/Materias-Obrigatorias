###Jogo os Palpites###
print("Bem-vindo ao Jogo dos Palpites") 
x = str(input("Jogador 1 - Digite seu nome: "))
y = str(input("Jogador 2 - Digite seu nome: "))
print()
print(x, "escolha um número inteiro entre 1 e 20 para que", y, "possa adivinhar")
z = int(input("Digite o número escolhido: "))
print(y, "você tem  três palpites para tentar adivinhar um número inteiro entre 1 e 20 escolhido por", x)  
print()
p1 = int(input("Digite o primeiro palpite: "))
if p1 == z:
    print(y, "venceu, o número escolhido por", x, "foi", z)
    print("Fim de Jogo")
elif p1 < z:
    print("O número escolhido por", x, "foi maior")
    print()
    p2 = int(input("Digite o segundo palpite: "))
    if p2 == z:
        print(y, "venceu, o número escolhido por", x, "foi", z)
        print("Fim de Jogo")
    elif p2 < z:
        print("O número escolhido por", x, "foi maior")
        print()
        p3 = int(input("Digite o terceiro palpite: "))
        if p3 == z:
            print(y, "venceu, o número escolhido por", x, "foi", z)
            print("Fim de Jogo")
        elif p3 < z:
            print(y, "perdeu, o número escolhido por", x, "foi", z)
            print("Fim de Jogo")
        else:
            print(y, "perdeu, o número escolhido por", x, "foi", z)
            print("Fim de Jogo")
    else:
        print("O número escolhido por", x, "foi menor")
        print()
        p3 = int(input("Digite o terceiro palpite: "))
        if p3 == z:
            print(y, "venceu, o número escolhido por", x, "foi", z)
            print("Fim de Jogo")
        elif p3 < z:
            print(y, "perdeu, o número escolhido por", x, "foi", z)
            print("Fim de Jogo")
        else:
            print(y, "perdeu, o número escolhido por", x, "foi", z)
            print("Fim de Jogo")
else:
    print("O número escolhido por", x, "foi menor")
    print()
    p2 = int(input("Digite o segundo palpite: "))
    if p2 == z:
        print(y, "venceu, o número escolhido por", x, "foi", z)
        print("Fim de Jogo")
    elif p2 < z:
        print("O número escolhido por", x, "foi maior")
        print()
        p3 = int(input("Digite o terceiro palpite: "))
        if p3 == z:
            print(y, "venceu, o número escolhido por", x, "foi", z)
            print("Fim de Jogo")
        elif p3 < z:
            print(y, "perdeu, o número escolhido por", x, "foi", z)
            print("Fim de Jogo")
        else:
            print(y, "perdeu, o número escolhido por", x, "foi", z)
            print("Fim de Jogo")
    else:
        print("O número escolhido por", x, "foi menor")
        print()
        p3 = int(input("Digite o terceiro palpite: "))
        if p3 == z:
            print(y, "venceu, o número escolhido por", x, "foi", z)
            print("Fim de Jogo")
        elif p3 < z:
            print(y, "perdeu, o número escolhido por", x, "foi", z)
            print("Fim de Jogo")
        else:
            print(y, "perdeu, o número escolhido por", x, "foi", z)
            print("Fim de Jogo")
    
       
