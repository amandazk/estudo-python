from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    # Para cada cenário de teste, a classe TestAvaliador vai invocar o método setUp
    def setUp(self):
        self.amanda = Usuario("Amanda")
        self.lance_amanda = Lance(self.amanda, 200)
        self.leilao = Leilao("Computador")

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.joao = Usuario("Joao")
        lance_joao = Lance(self.joao, 75)

        self.leilao.propoe(lance_joao)
        self.leilao.propoe(self.lance_amanda)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 75
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        joao = Usuario("Joao")
        lance_joao = Lance(joao, 75)

        self.leilao.propoe(self.lance_amanda)
        self.leilao.propoe(lance_joao)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 75
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_amanda)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(200, avaliador.menor_lance)
        self.assertEqual(200, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        joao = Usuario("Joao")
        ana = Usuario("Ana")
        lance_joao = Lance(joao, 75)
        lance_ana = Lance(ana, 900)

        self.leilao.propoe(self.lance_amanda)
        self.leilao.propoe(lance_joao)
        self.leilao.propoe(lance_ana)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 75
        maior_valor_esperado = 900

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
