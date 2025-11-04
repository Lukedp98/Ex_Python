# Exercício da média aritmética

# Variáveis
b1 = b2 = b3 = b4 = media = 0.0
nome = ""

# Entradas
nome = input("Informe o nome do aluno: ")
b1 = float(input("Informe a nota do primeiro bimestre: "))
b2 = float(input("Informe a nota do segundo bimestre: "))
b3 = float(input("Informe a nota do terceiro bimestre: "))
b4 = float(input("Informe a nota do quarto bimestre: "))

# Processamento
media = (b1 + b2 + b3 + b4) / 4

# Saída com duas casas decimais

if (media >= 7):
    print(f"O aluno {nome} teve a média final de {media:.2f} e foi Aprovado.")
elif (media >=6.5):
        print(f"O aluno {nome} teve a média final de {media:.2f} e está de Conselho de Classe.")
elif (media >=5):
    print(f"O aluno {nome} teve a média final de {media:.2f} e está de Recuperação.")
else:
    print(f"O aluno {nome} teve a média final de {media:.2f} e foi Reprovado.")