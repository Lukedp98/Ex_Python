def ola():
    nome=(input("Informe o nome: "))
    print ("ola", nome)

ola()

#Sem arg e com Retorno
def pi ():
    return 3.14
print(f"O valor de PI é: {pi()}")

# exercicio 2

def converterTemperatura ():
    temperatura = float(input("Informe a temperatura em Celsius: "))
    return (temperatura * 1.8) + 32
print(f"O valor da temperatura em Fahrenheit é {converterTemperatura ():.2f}")

# exercicio 7
def perCirculo (raio):
    return 2 * pi() * raio

r = float(input("Informe o raio: "))

print ("a Area é igual a:" , round(perCirculo(r),2))

# exercicio 8
def maiorValor (a, b):
    if (a==b): 
        return (a,b)
    elif(a>b):
        return (b)
    else:
        return (b)
    
a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))
print ("o maior valor é:", maiorValor (a, b))

def maiorValor2 (c, d):
    if (c>d): 
        res = "O maior valor é", c
    elif(c<d):
          res = "O maior valor é", d
    else:
        res = "Os valores são iguais"
        
    return res

c = int(input("Informe o valor de c: "))
d = int(input("Informe o valor de d: "))
print ("o maior valor é:", maiorValor2 (c, d))