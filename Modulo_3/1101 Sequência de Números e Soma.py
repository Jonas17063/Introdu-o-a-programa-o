while True:
    try:
        M, N = map(int, input().split())
        if M <= 0 or N <= 0:
            break

        inicio = min(M, N)
        fim = max(M, N)

        soma = 0
        linha = ""
        for i in range(inicio, fim + 1):
            linha += f"{i} "
            soma += i
        print(f"{linha}Sum={soma}")

    except EOFError:
        break
