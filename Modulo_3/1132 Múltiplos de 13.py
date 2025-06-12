# Lê os dois valores inteiros
X = int(input())
Y = int(input())

# Garante que a iteração será do menor para o maior
inicio = min(X, Y)
fim = max(X, Y)

soma = 0
for i in range(inicio, fim + 1):
    if i % 13 != 0:
        soma += i

print(soma)
