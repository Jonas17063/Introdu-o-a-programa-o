# Lê o número de casos de teste
N = int(input())

# Processa cada caso
for _ in range(N):
    a, b, c = map(float, input().split())
    media = (a * 2 + b * 3 + c * 5) / 10
    print(f"{media:.1f}")
