import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Meses fixos
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

# Função para gerar gráfico
def mostrar_grafico():
    try:
        pesos = [
            float(entry_jan.get()),
            float(entry_fev.get()),
            float(entry_mar.get()),
            float(entry_abr.get()),
            float(entry_mai.get()),
            float(entry_jun.get())
        ]
        
        # Criar gráfico
        plt.plot(meses, pesos, marker="o", linestyle="-", color="blue")
        plt.title("Evolução do Peso nos Últimos 6 Meses")
        plt.xlabel("Meses")
        plt.ylabel("Peso (kg)")

        # Mostrar valores no gráfico
        for i, valor in enumerate(pesos):
            plt.text(meses[i], valor, f"{valor}kg", ha="center", va="bottom")

        plt.show()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números válidos!")
# Criar janela principal
root = tk.Tk()
root.title("Registro de Peso")

# Criar entradas manualmente (sem laço)
tk.Label(root, text="Peso em Jan:").pack()
entry_jan = tk.Entry(root)
entry_jan.pack()

tk.Label(root, text="Peso em Fev:").pack()
entry_fev = tk.Entry(root)
entry_fev.pack()

tk.Label(root, text="Peso em Mar:").pack()
entry_mar = tk.Entry(root)
entry_mar.pack()

tk.Label(root, text="Peso em Abr:").pack()
entry_abr = tk.Entry(root)
entry_abr.pack()

tk.Label(root, text="Peso em Mai:").pack()
entry_mai = tk.Entry(root)
entry_mai.pack()

tk.Label(root, text="Peso em Jun:").pack()
entry_jun = tk.Entry(root)
entry_jun.pack()

# Botão para mostrar gráfico
tk.Button(root, text="Mostrar Gráfico", command=mostrar_grafico).pack(pady=10)

# Rodar interface
root.mainloop()
