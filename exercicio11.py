def negativo_imagem(imagem):
    # Cria uma nova imagem para armazenar
    negativo = []
    
    # Itera sobre cada linha da imagem
    for linha in imagem:
        # inverte os valores de cada pixel na linha
        nova_linha = [1 - pixel for pixel in linha]
        # Adiciona a nova linha a imagem negativa
        negativo.append(nova_linha)
        
    return negativo

imagem = [
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
]

print(negativo_imagem(imagem))