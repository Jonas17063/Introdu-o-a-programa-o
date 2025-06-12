# Lê o número de casos de teste
N = int(input())

# Processa cada caso
for _ in range(N):
    x, y = map(int, input().split())

    # Calcula os resultados das funções
    rafael = (3 * x) ** 2 + y ** 2
    beto = 2 * (x ** 2) + (5 * y) ** 2
    carlos = -100 * x + y ** 3

    # Determina o vencedor
    if rafael > beto and rafael > carlos:
        print("Rafael ganhou")
    elif beto > carlos:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")
