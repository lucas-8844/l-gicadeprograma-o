from random import randint

print("Jogo acerte o nomero")
numero_aleatorio = randint(1,10)
while True:
    numero = int(input("digite um numero de 1 a 10:"))
    if numero == numero_aleatorio:
        print("Parabens, você acertou!")
        break
    else:
        print("Errado, tente novamente")
    if numero > numero_aleatorio:
        print("tente um numero menor!")
    else:
     print("tente um numero maior!")

 

