import csv

# Função para ler o ficheiro e construir o dicionário
def ler_ficheiro_zoo(ficheiro):
    dicionario_animais = {}
    
    with open(ficheiro, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            nome_animal = row[0]
            classe_animal = row[1]
            
            if classe_animal not in dicionario_animais:
                dicionario_animais[classe_animal] = []
            
            dicionario_animais[classe_animal].append(nome_animal)
    
    return dicionario_animais

# Exemplo de uso
ficheiro = 'zoo.csv'
dicionario_animais = ler_ficheiro_zoo(ficheiro)

# Exibindo o dicionário
for classe, animais in dicionario_animais.items():
    print(f"Classe {classe}: {animais}")
