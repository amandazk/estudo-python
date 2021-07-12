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


class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas) 

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
mindhunter = Serie('Mindunter', 2019, 2)
rua_do_medo = Filme('Rua do Medo', 2021, 100)
ponyo = Filme('Ponyo - Uma amizade que veio do mar', 2008, 150)
atypical = Serie('Atypical', 2017, 4)

mindhunter.dar_like()
atypical.dar_like()
atypical.dar_like()
atypical.dar_like()
ponyo.dar_like()
ponyo.dar_like()

filmes_e_series = [vingadores, mindhunter, rua_do_medo, ponyo, atypical]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print('Tamanho da playlist : {}'.format(len(playlist_fim_de_semana)))

for programa in playlist_fim_de_semana:
    print(programa)