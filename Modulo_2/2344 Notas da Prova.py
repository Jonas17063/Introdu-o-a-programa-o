# Lê a nota como inteiro
nota = int(input())

# Verifica e imprime o conceito correspondente
if 86 <= nota <= 100:
    print("A")
elif 61 <= nota <= 85:
    print("B")
elif 36 <= nota <= 60:
    print("C")
elif 1 <= nota <= 35:
    print("D")
else:  # nota == 0
    print("E")
