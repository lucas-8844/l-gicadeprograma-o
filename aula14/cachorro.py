class Cachorro:
    def __init__(self,nome,cor,raca):
        self.nome = nome
        self.cor = cor
        self.raca = raca

cachorro1 = Cachorro(nome="thor",cor="caramelo",raca="viralata")
print(cachorro1)
        

class Gato:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

gato1 = Gato(nome="garfild",cor="laranja")
print(gato1)