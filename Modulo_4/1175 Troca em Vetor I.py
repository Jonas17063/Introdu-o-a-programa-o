n = []

# Leitura dos 20 valores
for _ in range(20):
    valor = int(input())
    n.append(valor)

# Troca dos elementos: i com 19 - i
for i in range(10):
    n[i], n[19 - i] = n[19 - i], n[i]

# Impressão do vetor resultante
for i in range(20):
    print(f"N[{i}] = {n[i]}")
