
class Livro:
    def __init__(self,titulo,anoPubli,autor):
        self.titulo = titulo
        self.anoPubli = anoPubli
        self.autor = autor
        self.emprestado = False

class Membro:
    def __init__(self,numero_membro,nome,ano_nasc):
        self.numero_membro = numero_membro
        self.nome = nome
        self.ano_nasc = ano_nasc
        self.historico_livros_emprestados = []


class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.membros = []

    def adiciona_livro(self,livro:Livro):
        self.catalogo.append(livro)
        print("livro adicionado ao catálago!")

    def emprestar_livro(self,livro:Livro,membro:Membro):
        if livro in self.catalogo and livro.emprestado == False and membro in self.membros:
            livro.emprestado = True
            membro.historico_livros_emprestados.append(livro)
        
    
    def devolver_livros(self,livro:Livro):
        if livro.emprestado == False:
            print("Livro ja está disponível")
        livro.emprestado = False
        print("Livro devolvido!")

    def cadastra_membro(self,membro:Membro):
        self.membros.append(membro)
        print("Membro cadastrado com sucesso")

    def listar_livros_disponiveis(self):
        print()
        print("="*30)
        print("Catalogo de livros disponíveis".center(30))
        print("="*30)
        for livro in self.catalogo == False:
            print(f"titulo:{Livro.titulo} - Autor: {Livro.autor} - Emprestado{Livro.emprestado}")

         
    
l1 = Livro("Morte e vida severina", "1987", "Joao Cabral de Melo Neto")
l2 = Livro("Dom Casmurro", "1987", "Machado de Assis")
m1 = Membro("010203", "joao Severino",2004)
b1 = Biblioteca()
b1.adiciona_livro(l1)
b1.adiciona_livro(l2)
b1.cadastra_membro(m1)
b1.emprestar_livro(l1,m1)
b1.emprestar_livro(l2,m1)
b1.devolver_livros(l1)
b1.devolver_livros(l2)
b1.listar_livros_disponiveis()
