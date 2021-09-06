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

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):
        amanda = Usuario("Amanda")

        lance = Lance(amanda, 200)

        leilao = Leilao("Celular")
        leilao.lances.append(lance)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(200, avaliador.menor_lance)
        self.assertEqual(200, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        amanda = Usuario("Amanda")
        joao = Usuario("Joao")
        ana = Usuario("Ana")

        lance_amanda = Lance(amanda, 200)
        lance_joao = Lance(joao, 75)
        lance_ana = Lance(ana, 900)

        leilao = Leilao("Computador")

        leilao.lances.append(lance_amanda)
        leilao.lances.append(lance_joao)
        leilao.lances.append(lance_ana)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 75
        maior_valor_esperado = 900

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
