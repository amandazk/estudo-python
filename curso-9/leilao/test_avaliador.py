from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_avalia(self):
        amanda = Usuario("Amanda")
        joao = Usuario("Joao")

        lance_amanda = Lance(amanda, 200)
        lance_joao = Lance(joao, 75)

        leilao = Leilao("Computador")

        leilao.lances.append(lance_joao)
        leilao.lances.append(lance_amanda)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 75
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
