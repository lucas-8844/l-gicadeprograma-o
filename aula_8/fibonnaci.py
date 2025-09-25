# - Crie uma função que receba um numero inteiro como parâmetro e retorna a sequencia fibonnaci ate aquela ordem respectiva.
def fibonacci(n):
    seq = [0, 1]
    while len(seq) < n:
        proximo = seq[-1] + seq[-2]
        seq.append(proximo)
    return seq[:n]  
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]