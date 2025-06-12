while True:
    m, n = map(int, input().split())
    
    if m == 0 and n == 0:
        break
    
    soma = m + n
    # Remove todos os zeros do número convertido para string
    resultado = str(soma).replace('0', '')
    
    print(resultado)
