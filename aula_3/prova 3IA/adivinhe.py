print("\n!TENTE ACERTAR O NUMERO!\n")
numero = int
numero_certo = 7
tentativas = 1
numero_tentativas = 3
while numero != numero_certo:
 while tentativas <= numero_tentativas:
        tentativas += 1
        numero = int(input("Digite um numero de 1 a 10 e acerte em 3 tentativas:"))
        if numero == numero_certo:
            print("Parabens, você acertou o número!")
        else:
            print("Errado, tente denovo:")
 if numero != numero_certo:
    print("Você não acertou em 3 tentativas, mas não fique triste, tente novamente na próxima!")
 break