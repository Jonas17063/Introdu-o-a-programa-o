entrada = input().strip()

# Tenta converter para inteiro
try:
    minutos = int(entrada)
    if minutos < 0:
        print("entrada inválida")
    else:
        if minutos < 200:
            preco = minutos * 0.20
        elif minutos < 400:
            preco = minutos * 0.18
        else:
            preco = minutos * 0.15
        print(f"{preco:.2f}")
except ValueError:
    # Se não for possível converter para inteiro, é inválido
    print("entrada inválida")
