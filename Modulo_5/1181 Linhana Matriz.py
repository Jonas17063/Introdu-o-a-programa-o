# solução corrigida para o “Linha da Matriz” (URI 1182)

def main():
    L = int(input())         # índice da linha (0 a 11)
    op = input().strip()     # 'S' para soma ou 'M' para média

    soma = 0.0
    # percorre cada elemento da matriz 12×12, lendo um float por vez
    for i in range(12):
        for j in range(12):
            x = float(input())
            if i == L:
                soma += x

    # se for média, divide por 12
    if op == 'M':
        soma /= 12.0

    # imprime com uma casa decimal
    print(f"{soma:.1f}")


if __name__ == "__main__":
    main()
