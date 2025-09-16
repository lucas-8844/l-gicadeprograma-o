lista_alunos = []
for i in range (5):
    dicionario_alunos = {}
    print("novo aluno")
    dicionario_alunos['nome'] = input('Digite o nome do aluno:')
    dicionario_alunos['nota'] = input('Digite a nota do aluno:')
    lista_alunos.append(dicionario_alunos)
aluno_maior_nota = max(lista_alunos, key=lambda x: x['nota'])
print(f"\nO aluno com maior nota é {aluno_maior_nota['nome']} com nota {aluno_maior_nota['nota']}")
for i in lista_alunos:
    print(i)
    
    