def maior_numero(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior
print(maior_numero([3, 5, 2, 8, 1]))
# - Crie uma função chamada maior_numero que receba uma lista de números e retorne o maior número da lista.