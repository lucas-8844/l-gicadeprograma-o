musicas = []
while True:
    print("1 - adicione uma musica")
    print("2 - sair")
    opcao = input("Digite sua opção:")
    if opcao == "1":
        nova_musica = input("Nome da musica: ")
        musicas.append(nova_musica)
    if opcao == "2":
        break
print("Aqui está sua plalits:")
for i in musicas:
    print(i)