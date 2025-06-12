# Lê o número de casos de teste
N = int(input())

# Processa cada número
for _ in range(N):
    X = int(input())
    soma_divisores = 0

    # Soma dos divisores próprios de X (excluindo o próprio número)
    for i in range(1, X):
        if X % i == 0:
            soma_divisores += i

    # Verifica se é perfeito
    if soma_divisores == X:
        print(f"{X} eh perfeito")
    else:
        print(f"{X} nao eh perfeito")
