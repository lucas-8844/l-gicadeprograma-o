tempo_servico = int(input("quantos meses de serviço o trabalhador tem:"))
valor_fgts = float(input("Digite o valor do FGTS: R$ "))
multa = 40

if tempo_servico > 12:
    valor_fgts = valor_fgts*multa/100
    print("O valor da multa sera de:", valor_fgts)
else:
    print("Não há multa, pois o tempo de serviço é igual ou inferior a 1 ano.")