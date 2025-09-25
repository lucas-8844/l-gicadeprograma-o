# - Crie uma função chamada calculadora que receba três parâmetros: dois números e uma operação (como uma string: "soma", "subtração", "multiplicação", "divisão"). A função deve retornar o resultado da operação escolhida entre os dois números.
def calculadora(num1, num2, operacao):
    if operacao == "soma":
        return num1 + num2
    elif operacao == "subtração":
        return num1 - num2
    elif operacao == "multiplicação":
        return num1 * num2
    elif operacao == "divisão":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero"
    else:
        return "Operação inválida"
print(calculadora(10, 5, "soma"))
print(calculadora(10, 5, "subtração"))
print(calculadora(10, 5, "multiplicação"))
print(calculadora(10, 5, "divisão"))