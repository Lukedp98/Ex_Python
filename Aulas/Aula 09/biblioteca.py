#Biblioteca no Python
import math
from math import pow,sqrt
#import numpy as np
import LucasDePaula as ximba
from LucasDePaula import dividir

print(f"Valor do Pi: {round(math.pi,2)}")
print(f"2 elevado ao cubo: {round(pow(2,3))}")
print(f"Raiz quadrada de 81: {sqrt(81)}")
#print(np.array[1,2,3,4])

nome = input("Informe seu nome: ")
print(ximba.boasVindas(nome))

v1 = int(input("Informe um valor qualquer: "))
v2 = int(input("Informe outro valor qualquer: "))
print(f"A Soma dos valores {v1} e {v2} é: {ximba.somar(v1,v2)}")

a = int(input("Informe o número : "))
b = int(input("Informe o divisor : "))
result = dividir(a,b)
print(f"Resultado da divisão de {a}/{b} é {result}")