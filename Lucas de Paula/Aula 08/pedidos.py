cardapio = (
"1 - Àgua", 
"2 - Batata Fria", 
"3 - Hot-Dog ", 
"4 - Misto Quente", 
"5 - Refrigentes",
"6 - Suco",
"7 - X-Burguer",
"8 - X-salada", 
"9 - X-Bacon", 
"10 - Sunday",) 

pedido = []
"""

pedido.append(cardapio[2])
pedido.append(cardapio[8])
pedido.append(cardapio[9])
pedido.append(cardapio[6])
pedido.append(cardapio[7])
print("Nosso cardápio é: ", cardapio)
print("O pedido escolhido foi: ", pedido)
"""

pedido.append(cardapio[int(input("Informe a opção: "))-1])
pedido.append(cardapio[int(input("Informe a opção: "))-1])
pedido.append(cardapio[int(input("Informe a opção: "))-1])
pedido.append(cardapio[int(input("Informe a opção: "))-1])
pedido.append(cardapio[int(input("Informe a opção: "))-1])
print("Produtos escolhidos no cardápio: ", pedido)