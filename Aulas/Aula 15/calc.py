import tkinter as tk
from tkinter import messagebox

# Função principal da calculadora
class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Simples")
        master.geometry("300x400")
        master.resizable(False, False)

        # Variáveis de controle
        self.expressao = ""

        # Campo de texto (display)
        self.display = tk.Entry(master, font=("Arial", 20), borderwidth=5, relief="sunken", justify="right")
        self.display.pack(pady=10, fill="x", padx=10)

        # Cria os botões
        botoes = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '**', '+'],
            ['C', '=']
        ]

        # Criação dinâmica dos botões
        for linha in botoes:
            frame = tk.Frame(master)
            frame.pack(expand=True, fill="both")
            for botao in linha:
                tk.Button(frame, text=botao, font=("Arial", 16),
                          command=lambda b=botao: self.clique(b)).pack(side="left", expand=True, fill="both")

    # Função chamada quando um botão é pressionado
    def clique(self, botao):
        if botao == "=":
            self.calcular()
        elif botao == "C":
            self.expressao = ""
            self.display.delete(0, tk.END)
        else:
            self.expressao += botao
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expressao)

    # Função para realizar o cálculo
    def calcular(self):
        try:
            resultado = eval(self.expressao)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(resultado))
            self.expressao = str(resultado)
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Divisão por zero não é permitida!")
            self.display.delete(0, tk.END)
            self.expressao = ""
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida!")
            self.display.delete(0, tk.END)
            self.expressao = ""


# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    Calculadora(root)
    root.mainloop()