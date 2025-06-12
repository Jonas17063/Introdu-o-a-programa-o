# Lê os valores de entrada
x, y = map(int, input().split())

# Verifica se está dentro da semi-quadra
if 0 <= x <= 432 and 0 <= y <= 468:
    print("dentro")
else:
    print("fora")
