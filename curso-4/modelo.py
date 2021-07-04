class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return '{} - {} - {} like(s)'.format(self._nome, self.ano, self._likes)

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # pega do construtor da classe mãe (Programa)
        self.duracao = duracao

    def __str__(self):
        return '{} - {} - {} min - {} like(s)'.format(self._nome, self.ano, self.duracao, self._likes)


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return '{} - {} - {} temporada(s) - {} like(s)'.format(self._nome, self.ano, self.temporadas, self._likes)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)

mindhunter = Serie('Mindunter', 2019, 2)
mindhunter.dar_like()
mindhunter.dar_like()

filmes_e_series = [vingadores, mindhunter]
for programa in filmes_e_series:
    print(programa)