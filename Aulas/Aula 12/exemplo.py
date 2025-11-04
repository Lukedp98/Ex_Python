import tkinter as tk
#from tkinter import Tk
comb=tk.Tk()        #criando a tela do app
comb.title("Melhor Combustivel 1.0")
comb.geometry("400x500")
comb.maxsize(800,600)
comb.minsize(300,400)
#funções dos botões
def executar():
    a=float(alc.get())
    g=float(gas.get())
    r=a/g
    if r>=0.7:
        resultado.set("GASOLINA")
    else:
        resultado.set("ALCOOL")
    
def limpar():
    alc.delete(0,tk.END)
    gas.delete(0,tk.END)
    resultado.set("")
    
#frame do topo do app
topo=tk.Frame(comb, bg="lime", padx=10, pady=10)
topo.pack(fill="x")
tk.Label(topo, text="Melhor Combustivel").grid(row=0, column=0)

#frame do conteúdo do app
conteudo=tk.Frame(comb, bg="white", padx=10, pady=10)
conteudo.pack(fill="both", expand=True)
tk.Label(conteudo, text="Alcool R$:", font=("Arial", 16)).grid(row=0, column=0, padx=5, pady=5)
alc=tk.Entry(conteudo)
alc.grid(row=0, column=1, padx=5, pady=5)
tk.Label(conteudo, text="Gasolina R$:", font=("Arial", 16)).grid(row=1, column=0, padx=5, pady=5)
gas=tk.Entry(conteudo)
gas.grid(row=1, column=1, padx=5, pady=5)
tk.Button(conteudo, text="Calcular", command=executar).grid(row=3, column=0, padx=5, pady=5)
tk.Button(conteudo, text="LIMPAR", command=limpar).grid(row=3, column=1, padx=5, pady=5)
#frame do rodapé do app
rodape=tk.Frame(comb, bg="pink", padx=10, pady=10)
rodape.pack(fill="x")
tk.Label(rodape, text="RESULTADO:", font=("arial", 16)).grid(row=0, column=1, padx=5, pady=5)
resultado=tk.StringVar()
tk.Label(rodape, textvariable=resultado, font=("arial", 18) ).grid(row=1, column=1)


comb.mainloop()     #exibe a tela do aplicativo












'''
entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado.set("")
'''