# Biblioteca nativa do python para sorteio de valores
import random

# Sorteio de numeros inteiros definidos entre um menor e um maior
numero = random.randint(1, 60)
print(numero) # Pode serr qualquer número de 1 a 60

# Sorteio de numeros decimais entre 0 e 1
decimal = random.random()
print(round(decimal,2))


# Sorteio de um valor determinado por uma lista
cores = ["Vermelho", "Verde", "Azul", 1, 2 , "Roxo"]
cor = random.choice(cores)
print (cor) # Pode ser "vermelho", "azul" ou "verde"


# Cria uma lista de uma quantidade de elementos definidos pelo usuário

numeros = list(range(1, 61))

sorteio = random.sample (numeros, 6)
print (sorteio)

# Embaralha os valores de uma lista e apresenta em ordens aleatórias
cartas = ["A", 2, 4,5, 6, 8, 10, "J", "Q", "K"]
random.shuffle(cartas)
print(cartas)

#Reoganiza valores de uma lista
valores = [8,12,5,371,9,101]
print(sorted(valores))

# Compara duas listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
comuns = list(set(lista1) & set(lista2))
print(comuns)