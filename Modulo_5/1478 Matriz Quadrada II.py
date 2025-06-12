def main():
    while True:
        N = int(input())
        if N == 0:
            break

        # gera e imprime a matriz N×N
        for i in range(N):
            # para cada coluna j, calcula abs(i-j)+1
            row = []
            for j in range(N):
                val = abs(i - j) + 1
                # campo de largura 3, alinhado à direita
                row.append(f"{val:>3}")
            # junta com um espaço e imprime
            print(" ".join(row))

        # linha em branco após cada matriz
        print()

if __name__ == "__main__":
    main()