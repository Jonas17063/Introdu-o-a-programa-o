# Lê os dados de entrada
p, j1, j2, r, a = map(int, input().split())

# Caso de roubo
if r == 1 and a == 1:
    print("Jogador 2 ganha!")
elif r == 1 and a == 0:
    print("Jogador 1 ganha!")
elif r == 0 and a == 1:
    print("Jogador 1 ganha!")
else:
    # Jogo normal: sem roubo e sem acusação
    soma = j1 + j2
    if soma % 2 == 0:
        if p == 1:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
    else:
        if p == 0:
            print("Jogador 1 ganha!")
        else:
            print("Jogador 2 ganha!")
