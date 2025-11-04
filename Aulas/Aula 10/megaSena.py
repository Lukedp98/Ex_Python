import random
numeros = []
m = 0

while m < 6:
    numerosEscolhidos = int(input("Informe o número escolhido: "))
    numeros.append(numerosEscolhidos)
    m+=1
print(f"Números escolhidos: {sorted(numeros)}")

numerossorteados = list(range(1, 61))

sorteio = random.sample (numerossorteados, 6)
print (f"Números sorteados: {sorted(sorteio)}")

comum = list(set(numeros) & set(sorteio))
print(f"Números comuns{comum}")

if (len(comum) == 6):
    resultado = ("Novo Milinário")
elif (len(comum) == 5):
    resultado =("Parabéns. você acertou a Quina")
elif (len(comum) == 4):
    resultado = ("Tente outra vez")
elif (len(comum) == 3):
   resultado = ("Parar de jogar seu dinheiro fora")
elif (len(comum) == 2):
    resultado = ("Parabéns. você ganhou 2 reais")
elif (len(comum) == 1):
    resultado = ("Tu é muito burro")
else:
    resultado = ("Vai pra igreja seu azarado")
    
print(resultado)