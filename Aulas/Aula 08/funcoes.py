# Função sem argumento e sem retorno

def primeiraFuncao():
    print("Hello World!!")
    
# Invocando a função sem argumento e sem retorno
primeiraFuncao()

# ================

# Função com argumento e sem retorno
def somarValores(x,y):
    v1 = x
    v2 = y
    print(f"{v1} + {v2} = {v1 + v2}")

# Invocando a função com argumento e sem retorno
a=int(input("Digiteo primeiro valor: "))
b=int(input("Digiteo primeiro valor: "))
somarValores(a,b)

# Invocando a função sem argumento e com retorno

def mostrarTexto ():
    return "Ola, meu nome é ximbinha"
texto = mostrarTexto
# Invocando a função sem argumento 
print (texto())

#Função com argumento e com retorno
def areaQuad(x):
    return x**2
# Invocando a função com argumento 
z = int(input("Informe a medida que deseja calculcar: "))
print("Area ao Quadrado", areaQuad(z))