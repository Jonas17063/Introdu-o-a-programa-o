# Lê a quantidade de números
N = int(input())

# Lê a lista de N números inteiros
numeros = list(map(int, input().split()))

# Inicializa os contadores
m2 = m3 = m4 = m5 = 0

# Conta os múltiplos
for num in numeros:
    if num % 2 == 0:
        m2 += 1
    if num % 3 == 0:
        m3 += 1
    if num % 4 == 0:
        m4 += 1
    if num % 5 == 0:
        m5 += 1

# Imprime os resultados no formato solicitado
print(f"{m2} Multiplo(s) de 2")
print(f"{m3} Multiplo(s) de 3")
print(f"{m4} Multiplo(s) de 4")
print(f"{m5} Multiplo(s) de 5")
