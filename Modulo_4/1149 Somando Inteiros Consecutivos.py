valores = list(map(int, input().split()))

a = valores[0]
n = 0

# Procurar o primeiro valor positivo após o primeiro (que é A)
for v in valores[1:]:
    if v > 0:
        n = v
        break

soma = 0
for i in range(n):
    soma += a + i

print(soma)
