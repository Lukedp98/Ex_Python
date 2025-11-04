# Chamando biblioteca de criação de telas
import tkinter as tk 
from tkinter import messagebox

# Varial de criação do aplivativo
app = tk.Tk() # Cria a tela da interface 
app.title ("Exemplo de APP")
app.geometry ("1920x1080")
label=tk.Label(app, text="Olá mundo!!", font = "arial, 18")
label.pack()
texto=tk.Entry(app)
texto.pack()
def clique ():
    nome = texto.get()
    messagebox.showinfo("Bem Vindo!!!", "oi" + nome + "Olá você clicou no botão")
botao=tk.Button(app, text="Clique em mim", command= clique)
botao.pack()


app.mainloop() # Mantém a aplicação aberta