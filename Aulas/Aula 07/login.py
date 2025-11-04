usuario_correto = "Senai"
senha_correta = "Senai123"

usuario = (input("Informe o seu Usuário: "))
senha = (input("Informe sua senha: "))

if (usuario == "" or senha == ""):
    print ("Preencha os campos obrigatórios")
else:
    if (usuario == usuario_correto and senha == senha_correta):
        print ("Bem Vindo!!! Entrada autorizada")
    elif (usuario == usuario_correto and senha != senha_correta):
        print ("Entrada negada!!! Senha incorreta")
    elif (usuario != usuario_correto and senha == senha_correta):
        print ("Entrada negada!!! Usuário incorreto")
    else:
        print ("Entrada negada!!! Usuário e Senha incorretos")

"""
user = ""
password = ""
resp = ""

user = input ("Usuário:")
password = input ("Senha:")

if(user == "" or password ==""):
  print ("Preencha os campos obrigatórios")
else:
    if (user == "senai" and password == "senai123"):
        resp ("Bem Vindo!!! Entrada autorizada")
    elif (user == "senai" and password != "senai123"):
        resp ("Entrada negada!!! Senha incorreta")
    elif (user != "senai" and password == "senai123"):
        resp("Entrada negada!!! Usuário incorreto")
    else:
        resp ("Entrada negada!!! Usuário e Senha incorretos")
print(resp)
"""