horas_trabalhadas = int(input("quantas horas semanais foram trabalhadas ?"))
valor_hora = int(input("qual o valor de cada hora trabalhada ?"))


if horas_trabalhadas > 44:
    hora_extra = horas_trabalhadas - 44
    valor_extra = valor_hora/2 
    valor_extra = valor_hora + hora_extra
    print("horas extras trabalhadas:", hora_extra)
    print("Valor de cada hora extra: R$",valor_extra)
    print(hora_extra, "horas extras a R$", valor_extra, "cada.")