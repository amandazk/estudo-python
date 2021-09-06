from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
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

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        amanda = Usuario("Amanda")
        joao = Usuario("Joao")

        lance_amanda = Lance(amanda, 200)
        lance_joao = Lance(joao, 75)

        leilao = Leilao("Computador")

        leilao.lances.append(lance_amanda)
        leilao.lances.append(lance_joao)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 75
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
