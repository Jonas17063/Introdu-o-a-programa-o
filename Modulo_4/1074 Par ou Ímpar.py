n = int(input())

for _ in range(n):
    x = int(input())
    
    if x == 0:
        print("NULL")
    else:
        par_impar = "EVEN" if x % 2 == 0 else "ODD"
        sinal = "POSITIVE" if x > 0 else "NEGATIVE"
        print(f"{par_impar} {sinal}")
