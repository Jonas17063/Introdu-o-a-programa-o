c = int(input())

for _ in range(c):
    b, e = map(int, input().split())
    
    # Parte crescente da sequência
    crescente = ''.join(str(i) for i in range(b, e + 1))
    
    # Parte espelhada (invertida)
    espelho = crescente[::-1]
    
    # Resultado final
    print(crescente + espelho)
