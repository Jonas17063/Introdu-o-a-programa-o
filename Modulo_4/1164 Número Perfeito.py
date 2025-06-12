n = int(input())

for _ in range(n):
    x = int(input())
    soma = 0

    # Somar os divisores próprios de x
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            soma += i

    if soma == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")
