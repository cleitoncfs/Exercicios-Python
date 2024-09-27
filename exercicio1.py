#Função
def celsius_para_fahrenheit(celsius):
    fahrenheit = (9/5 * celsius) + 32
    return fahrenheit

# Solicitar a temperatura em celcius ao usuário
temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

# Converte para Fahrenheit
temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

# Resultado
print(f"A temperatura em Fahrenheit é: {temperatura_fahrenheit:.2f}°F")
