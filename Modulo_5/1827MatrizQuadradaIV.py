import sys

def processa(N):
    k = N // 3            # tamanho do “borda” externa
    c = N // 2            # índice do centro
    for i in range(N):
        linha = []
        for j in range(N):
            # 1) centro sempre ‘4’
            if i == c and j == c:
                linha.append('4')
            # 2) parte externa
            elif i < k or i >= N - k or j < k or j >= N - k:
                if i == j:
                    linha.append('2')
                elif i + j == N - 1:
                    linha.append('3')
                else:
                    linha.append('0')
            # 3) parte interna
            else:
                linha.append('1')
        print(''.join(linha))

for l in sys.stdin:
    l = l.strip()
    if not l:
        continue
    N = int(l)
    processa(N)
    print()
