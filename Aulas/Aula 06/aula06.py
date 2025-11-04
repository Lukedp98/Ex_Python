dia = int (input("Informe um numero referente ao dia da semana:"))
match(dia):
    case 1:
        print("domingo")
    case 2:
        print ("Segunda")
    case 3:
        print ("Terça")
    case 4:
        print ("Quarta")
    case 5:
        print ("Quinta")
    case 6:
        print ("Sexta")
    case 7:
        print ("Sabado")
    case _ :
        print ("Dia inválido")