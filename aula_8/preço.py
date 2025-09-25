# - Crie uma função desconto que receba o preço de um produto e um percentual de desconto (opcional, com valor padrão de 10%). A função deve retornar o preço com o desconto aplicado.
def desconto(preco, percentual=10):
    valor_desconto = preco * (percentual / 100)
    preco_com_desconto = preco - valor_desconto
    return preco_com_desconto       
print(desconto(100))  # Preço com desconto padrão de 10%
print(desconto(100, 20))  # Preço com desconto de 20%   