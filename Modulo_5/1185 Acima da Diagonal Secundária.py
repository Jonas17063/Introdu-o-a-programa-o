def main():
    op = input().strip()  # 'S' para soma ou 'M' para média

    soma = 0.0
    cont = 0

    # percorre cada posição da matriz 12×12, lendo um float por vez
    for i in range(12):         # i = índice da linha (0..11)
        for j in range(12):     # j = índice da coluna (0..11)
            valor = float(input())
            # só acumula se estiver acima da diagonal secundária:
            # coluna j < (11 - i)
            if j < 11 - i:
                soma += valor
                cont += 1

    # se for média, divide pela quantidade de elementos
    if op == 'M':
        soma /= cont

    # imprime resultado com 1 casa decimal
    print(f"{soma:.1f}")


if __name__ == "__main__":
    main()