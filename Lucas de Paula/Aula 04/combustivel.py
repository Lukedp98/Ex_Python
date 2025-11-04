g = a = cb = 0.0

a = float(input("informe o valor do alcool:"))
g = float(input("informe o valor da gasolina:"))

cb = (a/g)*100

# print (f"{cb:.2f}%")

if (cb >= 70):
    print (f"O custo beneficio é igual a {cb:.2f}% e o melhor combustivel é gasolina")
else:
    print (f"O custo beneficio é igual a {cb:.2f}% e o melhor combustivel é alcool")