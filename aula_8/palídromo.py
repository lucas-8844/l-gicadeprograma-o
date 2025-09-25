# - Crie uma função eh_palindromo que recebe uma string e retorna True se ela for um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente EXEMPLO NATAN), e False caso contrário.
def eh_palindromo(s):
    s = s.replace(" ", "").lower()  # Remove espaços e converte para minúsculas
    return s == s[::-1]  # Compara a string com sua reversa 
print(eh_palindromo("ovo"))  # True
print(eh_palindromo("Hello"))  # False