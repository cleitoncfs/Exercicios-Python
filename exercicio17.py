def produto_escalar(vetor1, vetor2, n):
    # Caso base: se o tamanho do vetor for 0, o produto escalar é 0
    if n == 0:
        return 0
    else:
        # Produto escalar dos elementos atuais mais o produto escalar dos elementos restantes
        return vetor1[n-1] * vetor2[n-1] + produto_escalar(vetor1, vetor2, n-1)

# Exemplo
vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
n = len(vetor1)

resultado = produto_escalar(vetor1, vetor2, n)
print(f"O produto escalar dos vetores é: {resultado}")
