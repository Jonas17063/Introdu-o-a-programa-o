idades = []
while True:
    idade = int(input())
    if idade < 0:
        break
    idades.append(idade)

media = sum(idades) / len(idades)
print(f"{media:.2f}")
