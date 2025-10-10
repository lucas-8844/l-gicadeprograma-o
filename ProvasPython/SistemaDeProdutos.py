
lista_produtos = []

def cadastro_de_produtos():
        dicionario = {}
        dicionario ["Nome:"] = input("Digite o nome do produto: ")
        dicionario ["preço"] = float(input("Digite o preço do produto: "))
        lista_produtos.append(dicionario)
        
def listarProdutos():
     if not lista_produtos:
        print("\n Nenhum produto cadastrado ainda.\n")
     else:
        for i in lista_produtos:
                print(i)

def filtrar_produtos():
    encontrou = False  

    for i in lista_produtos:
        if i["preço"] > 100:
            print(f"Produto: {i['Nome']:<20} | Preço: R$ {i['preço']:.2f}")
            encontrou = True

    if not encontrou:
        print("\nNenhum produto acima de R$100 encontrado.\n")
while True:
    print("Sistema de produtos.")
    print("Deseja cadastrar um produto ? digite 1")
    print("Deseja listar quais produtos existem ? digite 2")
    print("Deseja filtrar produtos caros ? digite 3")
    print("Deseja sair do sistema ? digite 4")
    opcao = input("Digite sua opção: ")
    if opcao == "1":
     cadastro_de_produtos()
     print("\n Produto cadastrado com sucesso!\n")
    elif opcao == "2":
     listarProdutos()
    elif opcao == "3":
        filtrar_produtos()
    elif opcao == "4":
        print("obrigado por utilizar nosso sistema!")
        break
    else:
        print("Opcão inválida, tente novamente!")
        