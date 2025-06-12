# Lê os valores de P e R
P, R = map(int, input().split())

# Verifica o caminho da bolinha
if P == 0:
    print("C")
else:
    if R == 0:
        print("B")
    else:
        print("A")
