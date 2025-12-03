class Produto:
    def __init__(self,nome,quantidade,preco_unitario):
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario
        self.total_produto_estoque = self.quantidade * self.preco_unitario


class Cliente:
    def __init__(self,nome,telefone):
        self.nome = nome
        self.telefone = telefone
        self.gasto_total = 0


class Estoque:
    def __init__(self):
        self.lista_clientes = []
        self.estoque_produtos = []

    def cadastra_produto(self,produto:Produto):
     if produto not in self.estoque_produtos:
      self.estoque_produtos.append(produto)
      print("Produto cadastrado com sucesso")
     else:
        print("Produto já cadastrado")
      

    def cadastra_cliente(self,cliente:Cliente):
     if cliente not in self.lista_clientes:
      self.lista_clientes.append(cliente)
      print("Cliente cadastrado com sucesso")
     else:
        print("Cliente já cadastrado!")


    def vender_produto(self,produto:Produto,cliente:Cliente,nome_produto,quantidade_vendida):
     if produto not in self.estoque_produtos:
        print("O Produto não está cadastrado")
     else:
        quantidade_vendida = int(input("Digite a quantidade que deseja comprar"))
        if produto.quantidade < quantidade_vendida:
           print("Não temos produtos suficientes no estoque.")
        produto.quantidade -= quantidade_vendida
        total_venda = quantidade_vendida * produto.preco_unitario
        cliente.gasto_total += total_venda
        print(f"Venda realizada com sucesso! Agora restam {produto.quantidade}")
    

    def gerar_estatistica(self,cliente:Cliente,produto:Produto):
       for cliente in self.lista_clientes and produto in self.estoque_produtos:
          print(f"Cliente: {cliente.nome}, Gasto total: R${cliente.gasto_total:.2f}")
          print(f"Produto: {produto.nome}, Quantidade em estoque: {self.quantidade}, Preço unitário: R${produto.preço_unitario:.2f}, Faturamento: {produto.total_venda}")
    
       