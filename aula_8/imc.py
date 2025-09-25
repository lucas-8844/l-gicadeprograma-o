# - Crie uma função calcular_imc que receba o peso e altura de uma pessoa e calcule o Índice de Massa Corporal (IMC), com valores padrões de peso 70 kg e altura 1.75 m.

peso = float(input("Digite seu peso em kg (padrão 70 kg): ") or 70)
altura = float(input("Digite sua altura em metros (padrão 1.75 m): ") or 1.75)

def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    return imc
print(calcular_imc(peso,altura))