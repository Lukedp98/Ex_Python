import csv
import os
import tkinter as tk
tela=tk.Tk()
tela.title("Cadastro")
tela.geometry("400x500")
#frames
topo=tk.Frame(tela, bg="black")
topo.pack(fill="x")
tk.Label(topo,text="SISTEMA DE CADASTRO SENAI 1.0").pack()
main=tk.Frame(tela, bg="grey")
main.pack(fill="both", expand=True)
tk.Label(main, text="Nome:", font=("arial", 12)).grid(row=0,column=0, padx=5, pady=5)
tk.Label(main, text="Telefone:", font=("arial", 12)).grid(row=0,column=1, padx=5, pady=5)
tk.Label(main, text="E-mail:", font=("arial", 12)).grid(row=0,column=2, padx=5, pady=5)
name=tk.Entry(main)
name.grid(row=1,column=0, padx=5, pady=5)
tel=tk.Entry(main)
tel.grid(row=1,column=1, padx=5, pady=5)
mail=tk.Entry(main)
mail.grid(row=1,column=2, padx=5, pady=5)


# Nome do arquivo
arquivo = "cadastro.csv"

# Verifica se o arquivo existe. Se não, cria com cabeçalho
if not os.path.exists(arquivo):
    with open(arquivo, "w", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nome", "telefone", "email"])

# Função para cadastrar uma pessoa
def cadastrar():
    nome = name.get()
    telefone = tel.get()
    email = mail.get()
    with open(arquivo, "a", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([nome, telefone, email])        
    print("Cadastro realizado com sucesso!\n")   
    name.delete(0, tk.END)
    tel.delete(0, tk.END)
    mail.delete(0, tk.END)
# Função para listar todos os cadastros
def listar():
    print("\nLista de Cadastros:")
    with open(arquivo, "r", encoding = "utf-8") as f:
        reader = csv.reader(f)
        for linha in reader:
            print(" | ". join(linha))
    print()
# Função para sair
def sair():
    tela.destroy()

foot=tk.Frame(tela, bg="black")
foot.pack(fill="x")
tk.Button(foot, text="CADASTRAR", command=cadastrar ).grid(row=0,column=0, padx=5,pady=5)
tk.Button(foot, text="LISTAR", command=listar ).grid(row=0,column=1, padx=5,pady=5)
tk.Button(foot, text="SAIR", command=sair ).grid(row=0,column=2, padx=5,pady=5)
# Menu simples
'''  while True:
        print("1. Cadastrar pessoa")
        print("2. Ver lista de contatos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar()            
        elif opcao == "2":
            listar()            
        elif opcao == "3":
            print("Saindo...")
            break                     
        else:
            print("Opção Inválida, tente novamente.\n")                   
listar()'''

tela.mainloop()