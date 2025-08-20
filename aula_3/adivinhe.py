import random
numero = int
numero_certo = random.randint(0,10)
tentativa = 0
print("tente acertar o numero certo:")
while numero != numero_certo:
        numero = int(input("escreva um numero de 1 a 10:"))
        tentativa += 1
        if numero == numero_certo:
         print(f"Parabéns, você acertou em {tentativa} tentativas!")
        elif numero > numero_certo:
             print("Muito Alto, tente um numero mais baixo:")
        else:
             print("muito baixo, tente um numero maior:")  
         



        

    
    


