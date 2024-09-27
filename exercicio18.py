def removedup(s):
    # Caso base: se a string estiver vazia ou tiver apenas um caractere, não há duplicatas
    if len(s) <= 1:
        return s
    
    # Se o primeiro caractere é igual ao segundo, removemos o primeiro e chamamos a função recursivamente
    if s[0] == s[1]:
        return removedup(s[1:])
    else:
        # Caso contrário, mantemos o primeiro caractere e chamamos a função recursivamente para o restante da string
        return s[0] + removedup(s[1:])

# Exemplo
resultado = removedup('aabccda')
print(resultado)  # Saída: abcda
