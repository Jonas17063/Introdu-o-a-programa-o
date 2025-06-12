# Lê o número de linhas
N = int(input())

num = 1  # número inicial

for _ in range(N):
    print(f"{num} {num+1} {num+2} PUM")
    num += 4  # pula para o próximo bloco de 4
