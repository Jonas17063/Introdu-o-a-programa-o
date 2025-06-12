'''
Faça um programa que leia os nomes e idades de 5 pessoas e diga qual é o nome da pessoa mais velha.
'''
nomes = []
idades = []

for i in range(5):
    nome = (input(f"Digite nome da {i+1}º pessoa: "))
    idade = int(input(f"Digite a idade da {i+1}º pessoa: ,", "anos"))
    nomes.append(nome)
    idades.append(idade)

indice = idades.index(max(idades))
print("A pessoa mais velha é:", nomes[indice])
