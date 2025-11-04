for l in range(1, 11):  # multiplicando
    print(f"\nTabuada do {l}:")
    for j in range(1, 11):  # multiplicador
        print(f"{l} x {j} = {l * j}")


for num3 in range (1,12):
    print(f"\n tabuada do {num3}: ")
    for mul in range (1,12):
        print (f"{num3} x {mul} = {num3 * mul}")
        
# Exemplo 1 tabuada 
num = int(input("Informe o numero da sua tabuada:"))
for n in range (1,11):
    print(f"{n}x{num} = {n*num}")
print("fim da tabuada do", num)

# Exemplo 2 tabuada
num2 = int(input("Informe o numero escolhido da tabuada"))
i=1
while (i<=10):
    print(f"{i}x{num2}={i*num2}")
    i+=1
print ("Fim da segunda tabuada")

for nt in range (1,6):
    print("sd", nt)