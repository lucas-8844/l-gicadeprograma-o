# - Crie uma função multiplicar_array que recebe uma array de números e retorna o produto de todos os elementos da array.


lista = []
while True :
    print("deseja adicionar numeros para sua lista ?")
    opcao = input("digite sim ou não!")
    if opcao == "sim":
        numero = int(input("Digite numero para sua lista: "))
        lista.append(numero)
    else:
        break
def multiplicar_array(lista):
    produto = 1
    for i in lista:
        produto *= i
    return produto
print("o produto dos numeros da sua lista eh:")
print(multiplicar_array(lista))


