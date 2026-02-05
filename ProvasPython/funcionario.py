class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def calcular_salario(self, horas_trabalhadas, valor_hora):
        self.salario = horas_trabalhadas * valor_hora
        return f"O salário do funcionário {self.nome} é {self.salario}"
    

class Gerente(Funcionario):
    def calcular_salario(self):
        func = Funcionario(nome = "maria", salario = 0)
        return self.salario


class Estagiario(Funcionario):
    def calcular_salario(self):
        return self.salario

    
        