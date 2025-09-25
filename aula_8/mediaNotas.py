# - Crie uma função chamada media que receba três notas de um aluno e calcule e retorne a média delas.
def media(nota1, nota2, nota3):
    soma = nota1 + nota2 + nota3
    media = soma/3
    return media
print(media(7,8,9))