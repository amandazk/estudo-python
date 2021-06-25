class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo do titular {} é {} reais".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

conta = Conta(123, "Amanda", 1000.0, 3000.0)
conta2 = Conta(133, "Carlos", 2500.0, 7000.0)

conta.extrato()
conta2.extrato()

conta2.deposita(1000.0)
conta2.extrato()
