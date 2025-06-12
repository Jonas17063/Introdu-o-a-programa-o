# Pré-calcula os 61 primeiros termos de Fibonacci (0 a 60)
fib = [0] * 61
fib[0] = 0
fib[1] = 1
for i in range(2, 61):
    fib[i] = fib[i - 1] + fib[i - 2]

# Lê o número de casos de teste
t = int(input())

# Processa cada caso
for _ in range(t):
    n = int(input())
    print(f"Fib({n}) = {fib[n]}")
