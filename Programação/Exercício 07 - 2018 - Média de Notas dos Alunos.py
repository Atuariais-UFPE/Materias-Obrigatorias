###Média dos Alunos###
turmas = int(input("Digite a quantidade de turmas: "))
media_turmas = 0
cont_turmas = 0
while cont_turmas < turmas:
    print()
    alunos = int(input("Digite a quantidade de alunos da turma: "))
    cont_alunos = 0
    media_parcial = 0
    while cont_alunos < alunos: 
        print()
        print("Digite as três notas do aluno", cont_alunos + 1)
        cont_alunos += 1
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        media_parcial += (nota1 + nota2 + nota3)/3
    print("A média desta turma é", media_parcial/alunos)
    cont_turmas += 1
    media_turmas += (media_parcial/alunos)/turmas
print()
print("A média das turmas é", media_turmas)    
    
