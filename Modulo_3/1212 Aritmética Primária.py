while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    carry = 0
    carry_count = 0

    while a > 0 or b > 0:
        d1 = a % 10
        d2 = b % 10

        if d1 + d2 + carry >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0

        a //= 10
        b //= 10

    # Imprime resultado de acordo com a contagem
    if carry_count == 0:
        print("No carry operation.")
    elif carry_count == 1:
        print("1 carry operation.")
    else:
        print(f"{carry_count} carry operations.")
