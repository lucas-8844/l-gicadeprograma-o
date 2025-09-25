# - Crie uma função par_ou_impar que receba um número e retorne uma string informando se o número é "par" ou "ímpar".
numero = int(input("Digite um número: "))
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
print(par_ou_impar(numero))
    