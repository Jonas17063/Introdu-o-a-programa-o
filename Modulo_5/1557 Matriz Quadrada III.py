def main():
    N = int(input())      # número de matrizes a processar
    idx = 4               # começamos em #4, pois as 3 primeiras já foram feitas

    for _ in range(N):
        M = int(input())  # ordem da matriz atual
        # lê a matriz A
        A = [list(map(int, input().split())) for __ in range(M)]
        # calcula o “quadrado” de A em B
        B = [[A[i][j] * A[i][j] for j in range(M)] for i in range(M)]

        # para cada coluna j, determina a largura (em caracteres) do maior valor em B[:,j]
        widths = [
            max(len(str(B[i][j])) for i in range(M))
            for j in range(M)
        ]

        # cabeçalho com o índice correto
        print(f"Quadrado da matriz #{idx}:")
        # imprime cada linha i da matriz B
        for i in range(M):
            for j in range(M):
                s = str(B[i][j])
                pad = widths[j] - len(s)
                if j == 0:
                    # primeira coluna: só padding + número
                    print(' ' * pad + s, end='')
                else:
                    # colunas seguintes: um espaço separador + padding + número
                    print(' ' + ' ' * pad + s, end='')
            print()
        # separa do próximo bloco (exceto após o último)
        if idx < 4 + N - 1:
            print()

        idx += 1

if __name__ == "__main__":
    main()

