
users = {}

while True:
    print("\n[1] Cadastrar novo usuário")
    print("[2] Fazer login")
    print("[3] Sair")
    op = input("Escolha: ").strip()

    if op == "1":
        username = input("Novo login: ").strip()
        if username in users:
            print(" Esse login já existe.")
        else:
            password = input("Nova senha: ")
            users[username] = password
            print(" Usuário cadastrado.")

    elif op == "2":
        username = input("Login: ").strip()
        password = input("Senha: ")
        # existe e a senha confere?
        if username in users and users[username] == password:
            print(" Login bem-sucedido!")
        elif username not in users:
            print(" Usuário não encontrado.")
        else:
            print(" Senha incorreta.")

    elif op == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")

        
             
