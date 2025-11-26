from datetime import datetime 
print()

class Conta:
    def __init__(self,numero_conta,titular):# Método construtor
        self.numero_conta = numero_conta
        self.titular = titular 
        self.saldo = 0
        self.data_criacao = datetime.now().date() 

class ContaCorrente(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
        self.cheque_especial = 400
    
    def sacar(self,valor_saque):
        # retirar o valor do saldo
        if self.saldo < valor_saque:
            print("Saldo insuficiente!")
            if self.saldo + self.cheque_especial < valor_saque:
                print("Cheque especial não cobre")
            else:
                self.saldo -= valor_saque
                print("Saque efetuado com sucesso! Cheque especial utilizado")

            return ""
        self.saldo -= valor_saque
        pass
    
    def depositar(self,valor_deposito:float):
        # adicionar o valor no saldo
        self.saldo += valor_deposito
        

    def transferir(self,conta_destinada:Conta,valor):
        # decrementa de uma conta e adiciona na outra
        if self.saldo < valor:
            print("Saldo insuficiente para transferência.")
            return "" 
        self.saldo -= valor 
        conta_destinada.saldo += valor
        print("Transferência efetuada com sucesso!") 

class ContaPoupanca(Conta):
    def __init__(self, numero_conta, titular):
        super().__init__(numero_conta, titular)
    
    def gerar_juros(self):
        # gera um juros de 1% sobre o saldo
        self.saldo += (1/100) * self.saldo
        pass 


# conta1 = ContaCorrente("010203","Joao Pescador")
# conta2 = ContaCorrente("010204","Gabriel")

# print("o valor do saldo da conta1 é igual a ",conta1.saldo)
# print("o valor do saldo da conta2 é igual a ",conta2.saldo)

# print(conta2.saldo)
# conta1.transferir(conta_destinada=conta2,valor=20)

# print(conta1.saldo)
# print(conta2.saldo)

contaPou = ContaPoupanca("010203","Gabriel")
contaPou.saldo = 1000
print(contaPou.saldo)
for i in range(30):
    contaPou.gerar_juros()
print(contaPou.saldo*12)