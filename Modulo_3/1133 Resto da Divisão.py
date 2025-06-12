# Lê os dois valores inteiros
X = int(input())
Y = int(input())

# Garante que X seja o menor e Y o maior
inicio = min(X, Y)
fim = max(X, Y)

# Itera do valor imediatamente após o menor até o valor imediatamente antes do maior
for i in range(inicio + 1, fim):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
