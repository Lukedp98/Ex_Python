import tkinter as app

boletim=app.Tk()
boletim.title("Boletim SENAI 1.23")
boletim.geometry("1000x200")

#funções
def media():
    b1=float(bim1.get())
    b2=float(bim2.get())
    b3=float(bim3.get())
    b4=float(bim4.get())
    media=(b1+b2+b3+b4)/4
    sit=""
    if media>=7:
        sit="APROVADO"
    elif media>=5:
        sit="RECUPERAÇÃO"
    elif media>4.5:
        sit="CONSELHO DE SALA"
    else:
        sit="REPROVADO"
    mf.set(media)
    resp.set(sit)
def limpar():
    bim1.delete(0,app.END)
    bim2.delete(0,app.END)
    bim3.delete(0,app.END)
    bim4.delete(0,app.END)
    mf.set("")
    resp.set("")

#topo app
topo=app.Frame(boletim, bg="red")
topo.pack(fill="x")

app.Label(topo, text="Boletim Python 60hr").pack()

#conteudo app
main=app.Frame(boletim, bg="white")
main.pack(fill="both", expand=True)

app.Label(main, text="1 Bim.", font=("arial",14) ).grid(row=0,column=0, padx=5, pady=5)
app.Label(main, text="2 Bim.", font=("arial",14) ).grid(row=0,column=1, padx=5, pady=5)
app.Label(main, text="3 Bim.", font=("arial",14) ).grid(row=0,column=2, padx=5, pady=5)
app.Label(main, text="4 Bim.", font=("arial",14) ).grid(row=0,column=3, padx=5, pady=5)

bim1=app.Entry(main, font=("arial", 14))
bim1.grid(row=1, column=0, padx=5, pady=5)
bim2=app.Entry(main, font=("arial", 14))
bim2.grid(row=1, column=1, padx=5, pady=5)
bim3=app.Entry(main, font=("arial", 14))
bim3.grid(row=1, column=2, padx=5, pady=5)
bim4=app.Entry(main, font=("arial", 14))
bim4.grid(row=1, column=3, padx=5, pady=5)


#rodape app
fim=app.Frame(boletim, bg="black")
fim.pack(fill="x")
app.Button(fim, text="MÉDIA FINAL", command=media).grid(row=1, column=2, padx=5, pady=5)
app.Button(fim, text="LIMPAR DADOS", command=limpar).grid(row=1, column=3, padx=5, pady=5)
mf=app.IntVar()
mediaFinal=app.Entry(fim, font=("arial",14), textvariable=mf )
resp=app.StringVar()
mediaFinal.grid(row=3, column=2, padx=5, pady=5)
situacao=app.Entry(fim, font=("arial",14), textvariable=resp )
situacao.grid(row=3, column=3, padx=5, pady=5)


boletim.mainloop()