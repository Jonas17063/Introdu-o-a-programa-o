# Lê os dados da entrada
dia_inicio = int(input().split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(" : "))
dia_fim = int(input().split()[1])
hora_fim, minuto_fim, segundo_fim = map(int, input().split(" : "))

# Converte tudo para segundos
segundos_inicio = dia_inicio * 24 * 3600 + hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio
segundos_fim = dia_fim * 24 * 3600 + hora_fim * 3600 + minuto_fim * 60 + segundo_fim

# Calcula a diferença
duracao = segundos_fim - segundos_inicio

# Converte de volta para dias, horas, minutos e segundos
dias = duracao // (24 * 3600)
duracao %= (24 * 3600)

horas = duracao // 3600
duracao %= 3600

minutos = duracao // 60
segundos = duracao % 60

# Exibe o resultado
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
