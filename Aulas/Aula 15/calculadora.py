# Função que recebe os valores e executa os calculos
def calculadora():
    # Escopo de variáveis globais
    total = 0.0 # Exibe o Resultado 
    pV = "" # Variável do primeiro valor
    Sv = 0.0 # Variável do dos valores até p usuário terminar as operações
    op = "" # Guardar o operador matemático escolhido
    # Laço que fica perguntando valores
    while True:
        if pV == "":
            pV = float(input("Informe o primeiro valor: "))
            total = pV;
        else: 
            op = input(" Digite um operador: (=,- , *, /, **) ou igual para finalizar os calculos ")
            
            if op == "=":
                print(f"Resultado:{total}")
                break
            else:
                sV = float(input("Informe o próximo valor:"))
                
                # Dependendo do operador...
                if op == "+":
                    total +=sV
                elif op == "-":
                    total -=sV
                elif op == "*":
                    total *=sV
                elif op == "**":
                    total **=sV
                elif op == "/":
                    if sV ==0:
                        print("Não é possível dividir por Zero")
                    else: 
                        total/=sV
                else:
                    print("Operação inválida!!!")
# Chamando a função que calcula os valores
calculadora()