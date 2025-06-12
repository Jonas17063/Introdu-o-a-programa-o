import math

n = int(input())

for _ in range(n):
    x = int(input())
    eh_primo = True

    if x < 2:
        eh_primo = False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                eh_primo = False
                break

    if eh_primo:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")
