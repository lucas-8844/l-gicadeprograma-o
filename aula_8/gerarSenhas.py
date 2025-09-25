# Faça um gerador de senhas aleatórias , que receba como parâmetros o tamanho da senha , que por padrão inicia em 6
import random
import string

def gerar_senha(tamanho=6):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
print(gerar_senha())  
print(gerar_senha(12))  