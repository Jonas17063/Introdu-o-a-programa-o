# Lê a quantidade de alunos
n = int(input())

# Variáveis para rastrear o melhor aluno
maior_nota = -1.0
matricula_maior = -1

# Lê os dados dos alunos
for _ in range(n):
    matricula, nota = input().split()
    nota = float(nota)
    
    if nota > maior_nota:
        maior_nota = nota
        matricula_maior = matricula

# Verifica a condição de nota mínima
if maior_nota >= 8.0:
    print(matricula_maior)
else:
    print("Minimum note not reached")
