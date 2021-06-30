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

   #método privado
    def __pode_sacar(self, valor_saque):
        valor_disponivel_para_saque = (self.__saldo + self.__limite)
        return valor_saque <= valor_disponivel_para_saque
            
    def saca(self, valor,):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor)) 

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        self.__limite
        print("O limite do titular é {} reais".format(self.__limite))

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

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

conta.limite = 4000.0
conta.limite

conta.saca(100.0)
conta.extrato()
conta.saca(5050.0)
conta.extrato()