import random 
clientes = []
while True:
    print("="*30)
    print("Cadastro de clientes")
    print("="*30)
    print("Deseja fazer um cadastro de um cliente ?")
    opcao = input("Digite sim ou não:")
    dicionario = {}
    if opcao == "sim":
        dicionario = {}
        dicionario['nome'] = input("Digite seu nome:")
        dicionario['email'] = input("Digite seu email:")
        dicionario['contato'] = input("digite seu contato:")
        clientes.append(dicionario)
    elif opcao == "não":
        break
    else:
        print("Digite uma opção válida!")
clienteAleatorio = random.choice(clientes)
print(clienteAleatorio)
            