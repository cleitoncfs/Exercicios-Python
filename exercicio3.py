# Função para calcular o valor do polinômio
def calcular_polinomio(x):
    return x**4 + x**3 + 2*x**2 - x

# Pontos a serem calculados
pontos = [1.1, 5, 2/3]

# Calcula e exibe o valor do polinômio em cada ponto
for ponto in pontos:
    valor = calcular_polinomio(ponto)
    print(f"O valor do polinômio em x = {ponto} é {valor:.2f}")
