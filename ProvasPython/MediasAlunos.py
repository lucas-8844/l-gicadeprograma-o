
alunos = {}

while True:
    nome = input("Nome do aluno: ")
    nota = float(input("Nota: "))
    alunos[nome] = nota  

    opcao = input("Deseja adicionar mais alunos? (s/n): ")
    if opcao.lower() == 'n':
        break
soma = sum(alunos.values())      
media = soma / len(alunos)

print(f"A média das notas dos alunos é: {media:.2f}")


        