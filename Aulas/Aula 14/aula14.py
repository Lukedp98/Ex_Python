teste="Aula 14" #variável de escopo global
#num=""
#criação da função
def exemplo():
    print (teste)   #pintar o texto da variável
    num=input("digite um numero: ")
    return num
#chamando a função exemplo
#exemplo()

print (exemplo())
'''
try:
    v1=float(input("Informe um valor: "))
    v2=float(input("Informe o divisor: "))
    res=v1/v2
    print (f"Resultado {round(res,2)}")
   
except ZeroDivisionError:
    print("Não é possível dividir por zero")
'''
res = 0
v1=float(input("Informe um valor: "))
v2=float(input("Informe o divisor: "))

if(v2 == 0):
    print("Não é possível dividir por zero")
else:
    res=v1/v2
print (f"Resultado {round(res,2)}")