def tabuada (v):
    while v <=10:
        print(f"\nTabuada do {v}:")
        i = 1
        while i <=10:
            print(f"{v} x {i} = {v*i}")
            i+=1
        v+=1
       
num1 = int(input("Informe um número de 1 a 10: "))
tabuada(num1)

# Exemplo 2 

def exemplotabuada (l):
    
    for l in range(l, 11):  # multiplicando
        print(f"\nTabuada do {l}:")
        for j in range(1, 11):  # multiplicador
            print(f"{l} x {j} = {l * j}")
              
num2 = int(input("Informe um número de 1 a 10: "))
exemplotabuada(num2)