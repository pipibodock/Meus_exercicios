class Conta_Corrente:

    def __init__(self, numero_da_conta, correntista, saldo=0):
        self.correntista = correntista
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo

    def altera_correntista(self, novo_correntista):
        self.correntista = novo_correntista

    def deposito(self, valor_do_deposito):
        self.saldo += valor_do_deposito

    def saque(self, valor_do_saque):
        if valor_do_saque > self.saldo:
            print('saldo insuficiente')
        else:
            self.saldo -= valor_do_saque 
        
Conta_Corrente(123, 'fellipe').altera_correntista('luiz')
Conta_Corrente(123, 'fellipe', 10).saque(11)
