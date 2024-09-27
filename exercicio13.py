def inverter_dicionario(dicionario):
    dicionario_invertido = {}
    
    for chave, valor in dicionario.items():
        if valor not in dicionario_invertido:
            dicionario_invertido[valor] = [chave]
        else:
            dicionario_invertido[valor].append(chave)
    
    return dicionario_invertido

# Exemplo
dicionario_original = {'joao': 10, 'pedro': 18, 'tiago': 13, 'luis': 18}
dicionario_resultado = inverter_dicionario(dicionario_original)

print(dicionario_resultado)
