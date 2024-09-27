# Abre (ou cria) o ficheiro em modo de escrita
with open('primeiro.txt', 'w') as ficheiro:
    # Escreve o conteúdo no ficheiro
    ficheiro.write("Acabei de criar o meu primeiro ficheiro em Python.\n")
    ficheiro.write("Talvez tenha jeito para isto\n")

print("Ficheiro criado com sucesso!")
