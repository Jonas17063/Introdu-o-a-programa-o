'''
Leia uma matriz 3x3 de números inteiros e imprima a soma dos elementos de cada linha.
'''
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        n = int(input(f"M[{i}][{j}]: "))
        linha.append(n)
    matriz.append(linha)

for i in range(3):
    soma = sum(matriz[i])
    print(f"Soma da linha {i}: {soma}")
