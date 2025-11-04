import matplotlib.pyplot as plt
import tkinter as tk

# Janela principal
tela = tk.Tk()
tela.title("Peso")
tela.geometry("400x500")

main = tk.Frame(tela, bg="black")
main.pack(fill="both", expand=True)

# Labels e Entrys
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]
entradas = []

for i, mes in enumerate(meses):
    tk.Label(main, text=f"Insira o valor de {mes}:", font=("Arial", 12)).grid(row=i, column=0, padx=5, pady=5, sticky="w")
    entrada = tk.Entry(main)
    entrada.grid(row=i, column=1, padx=5, pady=5)
    entradas.append(entrada)

# Função para gerar gráfico
def peso():
    valores = []
    for entrada in entradas:
        try:
            valor = float(entrada.get())
        except ValueError:
            valor = 0
        valores.append(valor)

    plt.bar(meses, valores, color='blue')
    plt.title("Evolução dos meses")
    plt.xlabel("Meses")
    plt.ylabel("Valores")
    plt.show()

# Botão
foot = tk.Frame(tela, bg="grey")
foot.pack(fill="x")
tk.Button(foot, text="Mostrar Gráfico", command=peso).grid(row=0, column=0, padx=5, pady=10)

tela.mainloop()