class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'O livro "{self.titulo}" foi emprestado.')
        else:
            print(f'O livro "{self.titulo}" não está disponível.')

    def devolver(self):
        self.disponivel = True
        print(f'O livro "{self.titulo}" foi devolvido.')


class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def pegar_livro(self, livro):
        livro.emprestar()

    def devolver_livro(self, livro):
        livro.devolver()
