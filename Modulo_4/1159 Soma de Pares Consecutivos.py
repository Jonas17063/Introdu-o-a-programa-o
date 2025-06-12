while True:
    x = int(input())
    if x == 0:
        break

    if x % 2 != 0:
        x += 1  # Se for ímpar, começa do próximo par

    soma = 0
    for i in range(5):
        soma += x + 2 * i  # Soma os 5 pares consecutivos

    print(soma)
