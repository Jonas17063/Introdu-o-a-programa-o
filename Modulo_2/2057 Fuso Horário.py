# Lê os três inteiros da entrada
S, T, F = map(int, input().split())

# Calcula a hora de chegada com ajuste de fuso
hora_chegada = (S + T + F) % 24

# Exibe o resultado
print(hora_chegada)
