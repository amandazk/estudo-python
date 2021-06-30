class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome

# por causa do @property, quando for chamar a função nome, não preciso colocar os parenteses
cliente = Cliente("amanda")
cliente.nome = "amanda"
cliente.nome