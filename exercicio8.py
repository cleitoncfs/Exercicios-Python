def pertence_fibonacci(n):
    # Os dois primeiros números da sequência de Fibonacci
    a, b = 1, 1
    
    # Verifica se o número é um dos dois primeiros
    if n == a or n == b:
        return True
    
    # Gera a sequência até encontrar ou ultrapassar o número
    while b < n:
        a, b = b, a + b
    
    # Verifica se o número foi encontrado na sequência
    return b == n

# Teste com um número
numero = int(input("Digite um número: "))

if pertence_fibonacci(numero):
    print(f'O número {numero} pertence à sequência de Fibonacci.')
else:
    print(f'O número {numero} não pertence à sequência de Fibonacci.')
