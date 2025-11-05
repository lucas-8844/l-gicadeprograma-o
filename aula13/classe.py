class Pessoa:
    def __init__(self,nome,altura,idade,peso):
        self.nome= nome
        self.altura = altura
        self.idade = idade
        self.peso = peso

p1 = Pessoa(nome="Matheus",altura=1.75,idade=16,peso="pena")

print(type(p1.idade))
print(type(p1.nome))

# façam uma classe para representar um cachorro
# - caracteristicas
# - nome
# - cor
# - raça

class Cachorro:
    def __init__(self,nome,cor,raca):
        self.nome= nome
        self.cor= cor
        self.raca= raca
    def latir(self):
        return "ruufs"

C1 = Cachorro(nome="thor",cor="caramelo", raca = "vira-lata")

print(C1.nome)
print(C1.latir())

