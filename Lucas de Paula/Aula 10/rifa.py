from random import choice
nomes = [] #Lista de pyhton
c = 0 #Varial inicializadora laço while

while c<11:
    nome = input("Nome do comprador: ")
    nomes.append(nome)
    c+=1
print(f"Nomes no sortetio: {nomes}")
sorteado = choice(nomes)
print(f"Ganhador:{sorteado}")