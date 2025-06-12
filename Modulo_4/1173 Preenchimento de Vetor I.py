v = int(input())
n = [0] * 10  # Cria vetor com 10 posições

n[0] = v
for i in range(1, 10):
    n[i] = n[i - 1] * 2

for i in range(10):
    print(f"N[{i}] = {n[i]}")
