def pares_impares(lst):
    soma_pares = sum(x for x in lst if x % 2 == 0)
    soma_impares = sum(x for x in lst if x % 2 != 0)
    return (soma_pares, soma_impares)

# Teste
lst = [1, 4, 7, 9, 3, 2, 8, 5, 6, 11, 14, 32, 13, 44, 71, 1, 2]
resultado = pares_impares(lst)
print(resultado) 
