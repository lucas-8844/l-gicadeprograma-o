while True:
    salario = float(input("Qual é o salário mensal do trabalhador? "))
    meses = int(input("Qual é o número de meses trabalhados? "))

    if meses < 12:
        ferias = (salario * meses) / 12
        print(f"Férias proporcionais: R$ {ferias:.2f}")
    else:
        print("O trabalhador não tem direito a férias proporcionais.")

    repetir = input("Deseja calcular novamente? (s/n): ")
    if repetir.lower() != "s":
        break


