# Dados das frutas
frutas = {
    'maçã': {'quantidade_comprada': 100, 'preco_compra': 2.0, 'quantidade_stock': 80, 'preco_venda': 3.0},
    'banana': {'quantidade_comprada': 150, 'preco_compra': 1.0, 'quantidade_stock': 120, 'preco_venda': 1.5},
    'laranja': {'quantidade_comprada': 200, 'preco_compra': 1.5, 'quantidade_stock': 150, 'preco_venda': 2.5}
}


# Calculo do lucro
def calcular_lucro(frutas):
    lucro_total = 0
    for fruta, dados in frutas.items():
        quantidade_vendida = dados['quantidade_comprada'] - dados['quantidade_stock']
        lucro = quantidade_vendida * (dados['preco_venda'] - dados['preco_compra'])
        lucro_total += lucro
    return lucro_total

lucro = calcular_lucro(frutas)
print(f"Lucro já obtido: {lucro} euros")


# Encontrar a fruta mais cara
def fruta_mais_cara(frutas):
    fruta_cara = None
    maior_preco = 0
    for fruta, dados in frutas.items():
        if dados['preco_venda'] > maior_preco:
            maior_preco = dados['preco_venda']
            fruta_cara = fruta
    return fruta_cara

fruta_cara = fruta_mais_cara(frutas)
print(f"A fruta mais cara é: {fruta_cara}")
