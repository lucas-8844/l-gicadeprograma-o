alunos = []
for i in range (5):
    print('novo aluno')
    nome = input(f"Digite o nome do aluno : ")
    nota = input(f"Digite a nota do aluno : ")
    alunos.append((nome, nota))
aluno_maior_nota = max(alunos, key=lambda x: x[1])
print(f"\nO aluno com a maior nota é {aluno_maior_nota[0]} com nota {aluno_maior_nota[1]}")