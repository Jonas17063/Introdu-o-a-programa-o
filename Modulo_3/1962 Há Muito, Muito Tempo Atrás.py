# Lê a quantidade de casos
N = int(input())

# Processa cada caso
for _ in range(N):
    T = int(input())
    ano = 2015 - T
    
    if ano > 0:
        print(f"{ano} D.C.")
    else:
        print(f"{abs(ano - 1)} A.C.")
