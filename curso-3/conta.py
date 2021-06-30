class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero # __ serve para definir o atributo como privado
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O saldo do titular {} é {} reais".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

# Testes
conta = Conta(123, "Amanda", 1000.0, 3000.0)
conta2 = Conta(133, "Carlos", 2500.0, 7000.0)

conta.extrato()
conta2.extrato()

conta2.deposita(1000.0)
conta2.extrato()

conta.transfere(10.0, conta2)
conta.extrato()
conta2.extrato()