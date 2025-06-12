# Lista com os meses em inglês
meses = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Lê o número do mês
numero = int(input())

# Imprime o mês correspondente (ajustando o índice, que começa em 0)
print(meses[numero - 1])
