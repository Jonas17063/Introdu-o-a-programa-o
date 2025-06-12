'''
Escreva um programa que leia uma série de números inteiros positivos (um por vez). O programa deve continuar lendo até que o número 0 seja digitado. Em seguida, imprima:

-A quantidade de números digitados (sem contar o zero final)

-A soma total

-E a média dos números

📌 Exemplo de entrada:
5
3
2
0
📌 Exemplo de saída:
Quantidade: 3
Soma: 10
Média: 3.33

'''
contador = 0
num = int(input("Digite um número (negativo para sair): "))

while num >= 0:
    if num > 0:
        contador += 1
    num = int(input("Digite outro número (negativo para sair): "))

print("Quantidade de números positivos:", contador)
