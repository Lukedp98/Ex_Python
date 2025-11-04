peso = altura = imc = 0.0

peso = float(input("Informe o seu peso: "))
altura = float(input("Informe o sua altura: "))

imc = peso/(altura**2)

if (imc < 18.5 ):
    print (f"Seu IMC é {round(imc,2)} e você está Abaixo do Peso")
elif (imc < 24.9):
    print (f"Seu IMC é {round(imc,2)} e você está no peso Normal")
elif (imc < 29.9):
    print (f"Seu IMC é {round(imc,2)} e você está Sobrepeso")
elif (imc < 34.9):
    print (f"Seu IMC é {imc:.2f} e você está com Obesidade Grau I")
elif (imc < 39.9):
    print (f"Seu IMC é {imc:.2f} e você está com Obesidade Grau II")
else:
    print (f"Seu IMC é {round(imc,2)} e você está com Obesidade Grau III (mórbida)")