def main():
    C = int(input())        # índice da coluna (0 a 11)
    op = input().strip()    # 'S' para soma ou 'M' para média

    soma = 0.0
    # para cada elemento da matriz 12×12 (lido um float por linha)
    for i in range(12):         # i = 0..11 representa a linha
        for j in range(12):     # j = 0..11 representa a coluna
            x = float(input())
            if j == C:
                soma += x

    # se for média, divide a soma por 12
    if op == 'M':
        soma /= 12.0

    # imprime com 1 casa decimal
    print(f"{soma:.1f}")


if __name__ == "__main__":
    main()