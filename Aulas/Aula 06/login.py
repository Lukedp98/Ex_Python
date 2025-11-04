"""user = ""
password = ""
resp = ""

user = input ("Usuário:")
user = input ("Senha:")

if (user == "Senai" and password == "Senai123"):
    resp = "Bem vindo"
else:
    resp = "Entrada negada"
    """
# ==========

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