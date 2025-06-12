pares = 0

# Lê 5 valores inteiros
for _ in range(5):
    valor = int(input())
    if valor % 2 == 0:
        pares += 1

# Imprime o resultado
print(f"{pares} valores pares")
