class carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10

class bike:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 2 

carro1 = carro()
print(carro1.velocidade)
carro1.acelerar()
print(carro1.velocidade)

bike1 = bike()
print(carro1.velocidade)
bike1.acelerar()
print(carro1.velocidade)

