import zipfile
import os

# Criando e escrevendo (modo w) - sobrescreve tudo 
nome = input("Digite o nome do seu arquivo (ex: poema.txt): ")
caminho = "C:/Users/sn1038686/Documents/" + nome

with open(caminho, "w", encoding="utf-8") as f: 
    f.write("Batatinha quando nasce \n") 
    f.write("Espalha a rama pelo chão \n") 
    # \n cria uma quebra na linha após sua chamada

# Lendo para verificar (modo r)
with open(caminho, "r", encoding="utf-8") as f: 
    print("Conteúdo após modo w:\n", f.read())

# Adicionando mais conteúdo (modo a) - adiciona ao final do arquivo
with open("teste.txt", "a", encoding="utf-8") as f: 
    f.write("Menininha quando dorme \n")
    f.write("Põe a mão no coração. \n") 

# Lendo novamente para verificar 
with open("teste.txt", "r", encoding="utf-8") as f: 
    print("Conteúdo após modo a:\n", f.read())

# Apenas leitura (modo r)
with open("teste.txt", "r", encoding="utf-8") as f:
    conteudo = f.readlines()  # lê cada linha e coloca em uma lista

print("Conteúdo do arquivo lido com modo r:")
for linha in conteudo:
    print("-", linha.strip())  # strip remove a quebra de linha visual

# Criando um arquivo zip
arquivos_para_zipar = ["teste.txt", "ximbinha.txt", "colapso.txt", "xoelma.txt"]
with zipfile.ZipFile("meus_arquivos2.zip", "w") as z:
    for arquivo in arquivos_para_zipar:
        if os.path.exists(arquivo):
            z.write(arquivo)
        else:
            print(f"Aviso: '{arquivo}' não encontrado e não foi adicionado ao zip.")

print("Arquivos compactados em meus_arquivos2.zip")

# Descompactando arquivos
with zipfile.ZipFile("meus_arquivos2.zip", "r") as z:    
    z.extractall("descompactados")
print("Arquivos descompactados na pasta 'descompactados'")
