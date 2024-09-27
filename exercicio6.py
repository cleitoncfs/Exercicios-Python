def calcular_vencimento_liquido(vencimento_bruto):
    # Percentuais de desconto
    desconto_irs = 0.25
    desconto_seguranca_social = 0.11
    desconto_cna = 0.10
    
    # Cálculo dos descontos
    valor_irs = vencimento_bruto * desconto_irs
    valor_seguranca_social = vencimento_bruto * desconto_seguranca_social
    valor_cna = vencimento_bruto * desconto_cna
    
    # Cálculo do vencimento líquido
    vencimento_liquido = vencimento_bruto - (valor_irs + valor_seguranca_social + valor_cna)
    
    return vencimento_liquido

# Solicitar o vencimento bruto do usuário
vencimento_bruto = float(input("Digite o vencimento bruto: "))

# Calcular o vencimento líquido
vencimento_liquido = calcular_vencimento_liquido(vencimento_bruto)

# Exibir o resultado
print(f"O vencimento líquido é: {vencimento_liquido:.2f} euros")
