# - Crie uma função chamada saudar que recebe o nome de uma pessoa como parâmetro e retorna uma saudação personalizada (ex: "Olá, [nome]!").
nome = input("Digite seu nome: ")
def saudar(nome):
    return  f"Olá,{nome} seja bem vindo!"
print(saudar(nome))
