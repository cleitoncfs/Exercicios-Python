import math

def volume_cone(raio, altura):
    volume = (math.pi * raio**2 * altura) / 3
    return volume

# Solicita ao usuário o raio da base e a altura do cone
raio = float(input("Digite o raio da base do cone: "))
altura = float(input("Digite a altura do cone: "))

# Calculo do volume
volume = volume_cone(raio, altura)

# Resultado
print(f"O volume do cone é: {volume:.2f} unidades cúbicas")

