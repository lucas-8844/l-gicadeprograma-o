# Faça um gerador de senhas aleatórias , que receba como parâmetros o tamanho da senha , que por padrão inicia em 6
import random
import string

def gerar_senha(tamanho=6):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    senha_gerada = ""
    senha_gerada += senha
    return senha_gerada 
print(gerar_senha(15))

def descobridor_de_senha(senha):
    contador = 0
    while True:
        senha_gerada = ""
        for i in range(4):
           senha_gerada += str(random.randint(0,9))
        contador += 1
        print(senha_gerada)
        if senha_gerada == senha:
          print(f"foi descoberto em {contador} tentativas")
          print(f"acertou a senha é {senha_gerada}")
          break

print(descobridor_de_senha("1434"))



# def descibridor_senha(senha):
 #senha_gerada = ""
 #contador = 0
 #while senha_gerada != senha:
    #contador += 1
    #senha_gerada = ""       
 #for i in range(4):
    #senha_gerada += str(random.randint(0,9))

 #if senha_gerada == senha:
    #print(f"foi descoberto em {senha_gerada} tentativas")
    #senha_gerada = ""
   # print(random.randint(0,9))

#print(descibridor_senha("1234"))
