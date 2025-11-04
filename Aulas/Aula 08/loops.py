#Exibir os números de 1 a 5
for numero in range (1,6):
    print("Numero da sequência: ", numero)
    
print("Fim do laço For")

# exibir elementos da lista um por vez
lista = [1,5,7,11,4,8,9]

for i in lista:
    print("Valor do i: ", i)
print("Fim do laço com a lista")

# Mostrar números e seu dobro
numeros = [1,2,3,4]

for num in numeros:
    print(f"{num} x 2  = { num * 2}")
print("Fim do laço min tabuada")

# Somar todos os números de uma lista
valores = [5,8,2,10]
soma = 0
for v in valores:
    soma +=v
print(f"Soma total: {soma}")

#exemplo While com numeros fixos
contador = 0
while contador < 5:
    print(contador)
    contador +=1
print("Fim do laço While")
    
# exemplo de while criando um vetor
quantidade = int(input("Quantos valores deseja adicionar?: "))
valores = []
i = 0

while i < quantidade:
    valor = input(f"Digite o {i+1}º valor: ")
    valores.append(valor)
    i +=1
print("Lista criada:", valores)

# Exemplo de While com texto 
dados =[]
while True:
    item = input("Digite um valor(ou 'sair' para terminar): ")
    if item == 'sair':
        break
    dados.append(item)
    
print("Valores digitados: ", dados)