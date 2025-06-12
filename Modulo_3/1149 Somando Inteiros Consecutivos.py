# Lê todos os inteiros da linha
valores = list(map(int, input().split()))

A = valores[0]

# Encontra o primeiro N positivo após A
for N in valores[1:]:
    if N > 0:
        break

# Calcula a soma de A + (A+1) + ... + (A+N-1)
soma = 0
for i in range(N):
    soma += A + i

print(soma)
