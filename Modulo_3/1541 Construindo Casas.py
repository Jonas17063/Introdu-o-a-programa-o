import math

while True:
    entrada = input()
    if entrada.strip() == "0":
        break
    
    A, B, C = map(int, entrada.split())
    
    area_casa = A * B
    area_terreno = area_casa * 100 / C  # área total do terreno
    lado_terreno = math.sqrt(area_terreno)
    
    print(int(lado_terreno))  # truncar o valor (parte inteira apenas)
