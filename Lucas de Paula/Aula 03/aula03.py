# Comentário de uma linha no pythob

''''
Aula 03 de Python
Data: 23/09/2025
Tema: primeira aula d programação de Python
'''

'''
nome = "Lucas" # Criando variável do tipo string
v1 = int (input("Digite um valor")) # Criando variável do tipo inteiro
v2 = 2.5 # Criando variável do tipo float
v3 = int (input ("Digite um número inteiro qualquer:"))

print ("Hello world")
print ("Meu nome é" , nome)
print (f"{v3}x{v1}={v3*v1}")
'''

#calculadora 4 operações

#Entradas
n1 = float (input("Digite o primeiro valor:"))
n2 = float (input("Digite o segundo valor:"))

#Processamento das informações

soma = n1 + n2
subi = n1 - n2
multi = n1 * n2
if (n2 == 0):
    divi = "Não é possível dividir por ZERO"
else: 
    divi = n1 / n2
    
# Saídas

print (f"Soma de {n1} + {n2} = {soma:.2f}")
print (f"Subtração de {n1} - {n2} = {subi:.2f}")
print (f"Multiplicação de {n1} * {n2} = {multi:.2f}")
print (f"Divisão de {n1} / {n2} = {divi}")