# Faça um descobridor de senhas de 4 digitos.
def descobridor_senha(senha):
    for i in range(10000):
        tentativa = f"{i:04d}"  # Formata o número com 4 dígitos, preenchendo com zeros à esquerda
        if tentativa == senha:
            return tentativa
        print(f"foi descoberto em {tentativa} tentativas")
    return None 
print(descobridor_senha("0278"))  # Output: 0278