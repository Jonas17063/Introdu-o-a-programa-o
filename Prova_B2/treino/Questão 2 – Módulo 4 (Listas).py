'''
Leia 10 números inteiros e armazene-os em uma lista. Em seguida, exiba:

A lista original

A lista ao contrário

A soma de todos os elementos
'''

numeros = []

for i in range(10):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

print("Lista original:", numeros)
print("Lista invertida:", list(reversed(numeros)))
print("Soma dos elementos:", sum(numeros))
