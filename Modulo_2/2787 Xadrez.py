# Lê o número de linhas e colunas
L = int(input())
C = int(input())

# Verifica a cor da casa no canto inferior direito
if (L + C) % 2 == 0:
    print(1)  # Branca
else:
    print(0)  # Preta
