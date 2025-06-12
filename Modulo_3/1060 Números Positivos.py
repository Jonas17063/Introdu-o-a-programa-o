positivos = 0

# Lê 6 valores
for _ in range(6):
    valor = float(input())
    if valor > 0:
        positivos += 1

# Exibe o resultado
print(f"{positivos} valores positivos")
