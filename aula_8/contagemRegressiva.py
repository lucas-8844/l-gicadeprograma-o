# - Crie uma função chamada contagem_regressiva que recebe um número n e imprime os números de n até 1, em contagem regressiva.
import time
def contagem_regressiva(n):
    for i in range(n,0,-1):
        print(i)
        time.sleep(1)
contagem_regressiva(5)
#https://colab.research.google.com/drive/1hA-gUn3qr38VHmWFUBPpAzktx-a9EzD1