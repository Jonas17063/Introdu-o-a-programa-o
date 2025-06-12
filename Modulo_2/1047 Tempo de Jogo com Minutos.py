# Lê os valores de entrada
h_inicial, m_inicial, h_final, m_final = map(int, input().split())

# Converte tudo para minutos desde o início do dia
inicio_total_min = h_inicial * 60 + m_inicial
fim_total_min = h_final * 60 + m_final

# Calcula a duração
if fim_total_min > inicio_total_min:
    duracao_min = fim_total_min - inicio_total_min
elif fim_total_min < inicio_total_min:
    duracao_min = (24 * 60 - inicio_total_min) + fim_total_min
else:
    duracao_min = 24 * 60  # mesmo horário: 24 horas

# Converte para horas e minutos
horas = duracao_min // 60
minutos = duracao_min % 60

# Exibe o resultado
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
