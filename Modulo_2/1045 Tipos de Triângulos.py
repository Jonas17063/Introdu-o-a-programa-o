# Lê os três valores de ponto flutuante
valores = list(map(float, input().split()))

# Ordena os valores em ordem decrescente
valores.sort(reverse=True)
A, B, C = valores

# Verifica se forma triângulo
if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    # Verifica tipo de ângulo
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    elif A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    # Verifica tipo de lados
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")
