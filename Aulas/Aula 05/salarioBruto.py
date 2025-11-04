salario_bruto = salario_liquido = total_descontos = 0.0
dependentes = 0
vale_refeicao = 0.048
vale_transporte = 0.06
convenio_medico = 0.04

salario_bruto = float(input("informe o salário bruto: "))
dependentes = int(input("informe o número de dependentes: "))

INSS = 0.0

if (salario_bruto <= 1518.00):
    INSS = 0.075
    print (f"o desconto do INSS é {INSS:.3f}")
elif (salario_bruto <= 2793.88):
    INSS = 0.09
    print (f"o desconto do INSS é {INSS:.3f}")
elif (salario_bruto <= 4190.84):
    INSS = 0.12
    print (f"o desconto do INSS é {INSS:.3f}")
else:
    INSS = 0.14
    print (f"o desconto do INSS é {INSS:.3f}")
    
IRPF = 0.0

if (salario_bruto <= 1903.98):
    IRPF = 0.0
    print (f"o desconto do IRPF é {round(IRPF,3)}")
elif (salario_bruto <= 2826.65):
    IRPF = 0.075
    print (f"o desconto do IRPF é {round(IRPF,3)}")
elif (salario_bruto <= 3751.05):
    IRPF = 0.15
    print (f"o desconto do IRPF é {round(IRPF,3)}")
elif (salario_bruto <= 4664.68):
    IRPF = 0.225
    print (f"o desconto do IRPF é {round(IRPF,3)}")
else:
   IRPF = 0.275
   print (f"o desconto do IRPF é {round(IRPF,3)}")

desconto_convenio = convenio_medico * (1 + dependentes)
total_descontos = vale_refeicao + vale_transporte + desconto_convenio + INSS + IRPF
valor_descontos = salario_bruto * total_descontos
salario_liquido = salario_bruto - valor_descontos


print (f"o percentual de descontos é {round(total_descontos*100, 2)}%, o desconto do convênio é {round(desconto_convenio*100, 2)} o valor do desconto é {round(valor_descontos,2)} o salário liquido é {round(salario_liquido,2)}")