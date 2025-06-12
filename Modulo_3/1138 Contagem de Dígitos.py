def conta_digitos(n):
    contagem = [0] * 10
    fator = 1

    while n // fator > 0:
        menor = n - (n // fator) * fator
        digito = (n // fator) % 10
        maior = n // (fator * 10)

        for d in range(10):
            if d < digito:
                contagem[d] += (maior + 1) * fator
            elif d == digito:
                contagem[d] += maior * fator + menor + 1
            else:
                contagem[d] += maior * fator

        contagem[0] -= fator  # ajuste para não contar zeros à esquerda
        fator *= 10

    return contagem

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    if A > B:
        A, B = B, A

    total = conta_digitos(B)
    if A > 1:
        anterior = conta_digitos(A - 1)
        total = [t - a for t, a in zip(total, anterior)]

    print(" ".join(map(str, total)))
