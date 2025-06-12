def main():
    op = input().strip()  # 'S' para soma ou 'M' para média

    soma = 0.0
    cont = 0

    # lemos 144 valores, um por vez, para a matriz 12×12
    for i in range(12):         # i = 0..11 (linha)
        for j in range(12):     # j = 0..11 (coluna)
            x = float(input())
            # conta apenas os elementos **acima da diagonal principal** (j > i)
            if j > i:
                soma += x
                cont += 1

    # se for média, divide pela quantidade de elementos acima da diagonal
    if op == 'M':
        resultado = soma / cont
    else:
        resultado = soma

    # imprime com 1 casa decimal
    print(f"{resultado:.1f}")


if __name__ == "__main__":
    main()
