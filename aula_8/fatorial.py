#  - Crie uma função chamada fatorial que calcule o fatorial de um número.
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)      
print(fatorial(5))  # Output: 120