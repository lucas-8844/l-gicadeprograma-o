a = int(input("digite um valor para a:"))
b = int(input("digite um valor de b:"))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
        print(a)
