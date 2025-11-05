class Carro:
    def __init__(self,cor,modelo,ano):
        self.cor= cor
        self.modelo= modelo
        self.ano= ano
        self.velocidade= 0
    def freio(self):
        self.velocidade -= 3
        return f"O carro {self.modelo} freiou para {self.velocidade} km/h"
    def acelerar(self):
        self.velocidade += 8
        return f"O carro {self.modelo} freiou para {self.velocidade} km/h"

carro1= Carro(
    cor = input("digite a cor do carro:"),
    modelo = input("Digite o modelo do carro :"),
    ano = input("Digite o ano do carro:"))
carro2 = Carro(cor="azul",modelo="corsa",ano=2004)

print(carro1.modelo)
print(Carro.acelerar(carro1))
print(Carro.freio(carro1))
