# Cria o dicionário de DDDs
ddd_cidades = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

# Lê o DDD
ddd = int(input())

# Verifica se está cadastrado
if ddd in ddd_cidades:
    print(ddd_cidades[ddd])
else:
    print("DDD nao cadastrado")
