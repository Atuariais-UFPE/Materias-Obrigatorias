###Sequência Fibonacci###
n = int(input("Digite um número inteiro positivo: "))
cont = n
Fn1 = 1
Fn2 = 0
if n < 0:
    print("Número não compreendido dentro da sequência Fibonacci")
else:
    while cont >= 1:
        soma = Fn1 + Fn2
        Fn2 = Fn1
        Fn1 = soma
        cont -= 1
    print("A soma da sequência de Fibonacci de", n, "é", Fn1)
        
