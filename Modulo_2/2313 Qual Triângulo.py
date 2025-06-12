# Lê os três lados
a, b, c = sorted(map(int, input().split()))

# Verifica se é um triângulo válido pela desigualdade triangular
if a + b <= c:
    print("Invalido")
else:
    # Verifica tipo do triângulo
    if a == b == c:
        tipo = "Valido-Equilatero"
    elif a == b or b == c or a == c:
        tipo = "Valido-Isoceles"
    else:
        tipo = "Valido-Escaleno"
    
    print(tipo)
    
    # Verifica se é retângulo (Teorema de Pitágoras)
    if c**2 == a**2 + b**2:
        print("Retangulo: S")
    else:
        print("Retangulo: N")
