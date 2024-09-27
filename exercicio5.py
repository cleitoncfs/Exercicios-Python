def codificar(texto, distancia):
    resultado = ""
    for char in texto:
        if char.isalpha():
            # Verifica se o caractere é uma letra
            deslocamento = ord('a') if char.islower() else ord('A')
            # Calcula a nova posição do caractere
            novo_char = chr((ord(char) - deslocamento + distancia) % 26 + deslocamento)
            resultado += novo_char
        else:
            # Mantém caracteres não alfabéticos inalterados
            resultado += char
    return resultado

def descodificar(texto, distancia):
    # Para descodificar, basta inverter a distância
    return codificar(texto, -distancia)

# Solicitar o texto e a distância do usuário
texto = input("Digite o texto a ser codificado/descodificado: ")
distancia = int(input("Digite a distância: "))

# Codificar o texto
texto_codificado = codificar(texto, distancia)
print(f"Texto codificado: {texto_codificado}")

# Descodificar o texto
texto_descodificado = descodificar(texto_codificado, distancia)
print(f"Texto descodificado: {texto_descodificado}")
