def calcular_batimento_cardiaco_maximo(idade):
    # Fórmula para calcular o batimento cardíaco máximo
    batimento_maximo = 163 + 1.16 * idade - 0.018 * (idade ** 2)
    return batimento_maximo

# Solicitar a idade do usuário
idade = int(input("Digite a sua idade: "))

# Calcular o batimento cardíaco máximo
batimento_maximo = calcular_batimento_cardiaco_maximo(idade)

# Resultado
print(f"O valor médio do batimento cardíaco máximo para {idade} anos é: {batimento_maximo:.2f} bpm")
