a = int(input("digite um número inteiro para a:"))
b = int(input("digite um número inteiro para b:"))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
        print("o resultado é:",a,b)
