import tkinter as tk
from tkinter import messagebox

calc=tk.Tk()
calc.title("Calculadora Básica")
calc.geometry("400x400")
#valor 1
tk.Label(calc, text="Valor1: ").grid(row=0, column=0, padx= 3, pady=3)
txtValor1 = tk.Entry(calc)
txtValor1.grid(row=0, column=1, padx= 3, pady=3)
#valor 1
tk.Label(calc, text="Valor2: ").grid(row=1, column=0, padx= 3, pady=3)
txtValor2 = tk.Entry(calc)
txtValor2.grid(row=1, column=1, padx= 3, pady=3)
#Funções
def somar():
    v1=float(txtValor1.get())
    v2=float(txtValor2.get())
    somar=v1+v2
    resposta.set(somar)
    
def subtrair():
    v1=float(txtValor1.get())
    v2=float(txtValor2.get())
    subi=v1-v2
    resposta.set(subi)
    
    
def multiplicar():
    v1=float(txtValor1.get())
    v2=float(txtValor2.get())
    multi=v1*v2
    resposta.set(multi)
    
def Dividir():
    v1=float(txtValor1.get())
    v2=float(txtValor2.get())
    if (v2 == 0):
        resposta.set("Não é possível dividir por zero") #messagebox.showinfo(""Divisão", "Não é possível dividir por zero")  
    else:
        divi=v1/v2
        resposta.set(divi)
        
def Potencia():
    v1=float(txtValor1.get())
    v2=float(txtValor2.get())
    Pote=v1**v2
    resposta.set(Pote)
    
    

# Botões de comando
btnSomar= tk.Button(calc, text="+", command=somar, font ="arial, 10", width=2)
btnSomar.grid(row=2, column=0, padx= 3, pady=3)
btnSubtrair= tk.Button(calc, text="-", command=subtrair, font ="arial, 10", width=2)
btnSubtrair.grid(row=2, column=1, padx= 3, pady=3)
btnMultiplicar= tk.Button(calc, text="*", command=multiplicar, font ="arial, 10", width=2)
btnMultiplicar.grid(row=2, column=2, padx= 3, pady=3)
btnDividir= tk.Button(calc, text="/", command=Dividir, font ="arial, 10", width=2)
btnDividir.grid(row=2, column=3, padx= 3, pady=3)
btnPotencia= tk.Button(calc, text="**", command=Potencia, font ="arial, 10", width=2)
btnPotencia.grid(row=2, column=4, padx= 3, pady=3)

# Resultado
tk.Label(calc, text = "Resultado: ").grid(row=3, column=0, padx= 3, pady=3)
resposta=tk.StringVar()
tk.Label(calc, textvariable=resposta).grid(row=3, column=1, padx= 3, pady=3)
calc.mainloop()