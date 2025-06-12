try:
    while True:
        t = int(input())  # número de termos
        linha = input().split(" + ")
        
        termos_derivados = []
        
        for termo in linha:
            coef, exp = termo.split('x')
            coef = int(coef)
            exp = int(exp)
            
            novo_coef = coef * exp
            novo_exp = exp - 1
            
            if novo_exp == 1:
                termos_derivados.append(f"{novo_coef}x")
            else:
                termos_derivados.append(f"{novo_coef}x{novo_exp}")
        
        print(" + ".join(termos_derivados))

except EOFError:
    pass
