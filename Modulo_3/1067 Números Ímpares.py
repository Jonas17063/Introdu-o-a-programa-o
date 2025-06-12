# Lê o valor inteiro
X = int(input())

# Imprime os números ímpares de 1 até X
for i in range(1, X + 1):
    if i % 2 != 0:
        print(i)