valorCompra = ""
estadoCompra = ""
frete = ""

valorCompra = input("Informe o valor da compra: ")
estadoCompra = input("Informe o Estado da compra: ")

if (valorCompra > "100" or estadoCompra == "SP" or estadoCompra == "sp"):
    frete = ("Cupom de fretes gratis")
else:
    frete =  ("Frete para o seu estado de R$19,99")
    
print (frete)

valorCompra = "100"
estadoCompra = "SP"

valor = input("Informe o valor da compra: ")
estado = input("Informe o Estado da compra: ")

if (valor > valorCompra or estado == estadoCompra):
    print ("Cupom de fretes gratis")
else:
    print ("Frete para o seu estado de R$19,99")

# ==========

valorCompra = "100"
estadoCompra = "SP"

valor = input("Informe o valor da compra: ")
estado = input("Informe o Estado da compra: ")

if (valor > valorCompra or estado == estadoCompra):
    print ("Cupom de fretes gratis")
else:
    print ("Frete para o seu estado de R$19,99")