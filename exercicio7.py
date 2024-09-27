def sao_amigas(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    
    diferencas = sum(1 for a, b in zip(palavra1, palavra2) if a != b)
    limite = len(palavra1) * 0.1
    
    return diferencas < limite

# Teste com as palavras "comprimento" e "cumprimento"
palavra1 = "comprimento"
palavra2 = "cumprimento"

# Teste com as palavras "acento e assento"
# palavra1 = "acento"
# palavra2 = "assento"

if sao_amigas(palavra1, palavra2):
    print(f'As palavras "{palavra1}" e "{palavra2}" são amigas.')
else:
    print(f'As palavras "{palavra1}" e "{palavra2}" não são amigas.')
