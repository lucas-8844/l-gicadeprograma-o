nomes = ["Gabriel", "juliano", "Ana", "marcos"]

quantidade = 0
for nome in nomes:
    if nome.lower().startswith("a"):  # transforma tudo em minúsculo e verifica se começa com "a"
        quantidade += 1

print(f"O número de nomes que começam com a letra A é: {quantidade}")



#quantos nomes comecam com a letra a
