import math

# variaveis
v = r = h = 0.0

#entradas
r = float (input ("Informe o Raio do cilindro:"))
h = float (input ("Informe a altura do cilindro:"))

#processamento

v = (math.pi*(math.pow(r,2)))*h

#saidas

print (f"O valor do volume é {v:.2f}")
print(round(math.sqrt(v),2))