x = int(input())
y = int(input())

# Garante que x seja o menor e y o maior
inicio = min(x, y)
fim = max(x, y)

soma = 0
for i in range(inicio, fim + 1):
    if i % 13 != 0:
        soma += i

print(soma)
