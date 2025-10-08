from datetime import datetime 
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)

usuario = {}
usuario["nome"] = input("digite seu nome:")
usuario["data_criacao"] = datetime.now().date()

print(usuario)