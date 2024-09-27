def alterna_listas(list_a, list_b):
    # Cria uma lista vazia para armazenar o resultado
    resultado = []
    
    # Usa a função zip para iterar simultaneamente sobre ambas as listas
    for a, b in zip(list_a, list_b):
        resultado.append(a)
        resultado.append(b)
        
    return resultado

list_a = [1, 2, 3]
list_b = ['a', 'b', 'c']
print(alterna_listas(list_a, list_b))