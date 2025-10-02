def soma_par(*args):
    soma = 0
    for numero in args:
        if  numero%2==0:
            soma += numero
    return soma
print(soma_par(1,2,3,4,5))