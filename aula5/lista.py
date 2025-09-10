clientes = ["larica","gabriel","Anna","zé"]
print(clientes)
clientes.append("novo nome")
print(clientes)
clientes.remove("gabriel")
print(clientes)
clientes.pop(0)
print(clientes)
clientes[2] = "novo"
print(clientes)
indice = clientes.index("novo")
clientes = [indice]
print(clientes)
for i in clientes:
    print(i)