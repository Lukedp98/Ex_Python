media = ""
faltas = ""
result = ""

media = float(input("Informe a média do aluno: "))
faltas = int(input("Informe a quantidade de faltas do aluno: "))

if (media >= "7" and faltas < "4"):
    result = "Aluno Aprovado!"
else:
    result = "Aluno reprovado"
    
print (result)