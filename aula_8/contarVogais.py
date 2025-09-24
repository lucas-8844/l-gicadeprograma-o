def contar_vogais(palavra):
    quantidade = 0
    for letra in palavra:
        if letra.lower() in "aeiou":
            quantidade +=1
    return quantidade
print(contar_vogais("Ana"))