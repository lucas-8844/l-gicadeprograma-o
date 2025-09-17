notas = []
while True:
    print("1 - adicione um novo aluno")
    print("2 - sair")
    opcao = input("Digite sua opção:")
    dicionario = {}
    if opcao == "1":
        dicionario['nome'] = input("nome do aluno:")
        dicionario['nota'] = input("nota do aluno:")
    if opcao == "2":
        break
    if len(notas) > 0:
        soma = 0
        for aluno in notas:
            soma += aluno['nota']
    media = soma / len(notas)
    print(media)

    #notas = [10,9,8,10]
    #media = sum(notas) / len(notas)
    #print(media)