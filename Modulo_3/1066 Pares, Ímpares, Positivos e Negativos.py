# Inicializa os contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

# Lê os 5 valores
for _ in range(5):
    n = int(input())
    
    # Par ou ímpar
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Positivo ou negativo
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

# Imprime os resultados
print(f"{pares} valor(es) par(es)")
print(f"{impares} valor(es) impar(es)")
print(f"{positivos} valor(es) positivo(s)")
print(f"{negativos} valor(es) negativo(s)")
