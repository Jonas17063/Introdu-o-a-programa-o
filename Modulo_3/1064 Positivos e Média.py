positivos = 0
soma = 0.0

# Lê 6 valores
for _ in range(6):
    valor = float(input())
    if valor > 0:
        positivos += 1
        soma += valor

# Calcula a média
media = soma / positivos

# Exibe o resultado
print(f"{positivos} valores positivos")
print(f"{media:.1f}")
