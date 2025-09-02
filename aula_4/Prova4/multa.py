
salario = float(input("Digite o valor do salário: R$ "))
dias_atraso = int(input("Digite o número de dias de atraso: "))

multa = 0  

if dias_atraso > 5:
    for dia in range(6, dias_atraso + 1): 
        multa += salario * 0.02            
    print(f"\nAtraso de {dias_atraso} dias.")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("\nNão há multa, atraso igual ou inferior a 5 dias.")
