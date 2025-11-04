import matplotlib.pyplot as plt

# Dados de exemplo
x = [1, 2, 5, 4, 5]
y = [7, 4, 5, 3, 10]

# Criando o gráfico
plt.plot(x, y, marker = "o")  # linha com marcadores nos pontos
plt.title("Exemplo de Gráfico Simples")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Mostrar o gráfico
plt.show()

categorias = ["A","B","C","D","E","F"]
valores = [10, 15, 7, 12, 2.7, 10.0]

plt.bar(categorias, valores, color = 'skyblue')
plt.title("Exemplo de Gráfico de Barras")
plt.show()

valores = [30, 20, 25, 25]
labels = ["A","B","C","D"]

plt.pie(valores, labels=labels,autopct="%1.1f%%")
plt.title("Exemplo de Gráfico de Pizza")
plt.show()

# Usuário digita valores separodos por virgula
X = list(map(int, input("Digite os valores de x separados por vírgula: ").split(",")))

# Criar o gráfico
plt.plot(x, y, marker = "o")  # linha com marcadores nos pontos
plt.title("Gráfico simples com dados do usuário")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.show()