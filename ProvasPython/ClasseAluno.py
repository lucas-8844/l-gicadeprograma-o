class Aluno:
    def __init__(self,nome,notas,soma,media):
        self.nome=nome
        self.notas=notas
        self.media=media
    def calcular_media(self):
        self.media = sum(self.notas) / len(self.notas)
        return f"A média do aluno {self.nome} é {self.media}"

while True:
    opcao = input("Deseja adicionar um aluno? (s/n): ").lower()
    if opcao == "s":
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        aluno1 = Aluno(nome, [nota1, nota2])
        Aluno.append(aluno1)
        print(aluno1.calcular_media())
    else:
        break


