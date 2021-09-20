from unittest import TestCase
from dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):
    # Para cada cenário de teste, a classe TestLeilao vai invocar o método setUp
    def setUp(self):
        self.amanda = Usuario("Amanda")
        self.lance_amanda = Lance(self.amanda, 200)
        self.leilao = Leilao("Computador")

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.joao = Usuario("Joao")
        lance_joao = Lance(self.joao, 75)

        self.leilao.propoe(lance_joao)
        self.leilao.propoe(self.lance_amanda)

        menor_valor_esperado = 75
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(ValueError):
            joao = Usuario("Joao")
            lance_joao = Lance(joao, 75)

            self.leilao.propoe(self.lance_amanda)
            self.leilao.propoe(lance_joao)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_amanda)

        self.assertEqual(200, self.leilao.menor_lance)
        self.assertEqual(200, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        joao = Usuario("Joao")
        ana = Usuario("Ana")
        lance_joao = Lance(joao, 500)
        lance_ana = Lance(ana, 950)

        self.leilao.propoe(self.lance_amanda)
        self.leilao.propoe(lance_joao)
        self.leilao.propoe(lance_ana)

        menor_valor_esperado = 200
        maior_valor_esperado = 950

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # se o leilão não tiver lance, deve permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_um_lance(self):
        self.leilao.propoe(self.lance_amanda)

        quantidade_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_lances_recebido)

    # se o último usuário for diferente, dever permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        joao = Usuario("Joao")
        lance_joao = Lance(joao, 400)

        self.leilao.propoe(self.lance_amanda)
        self.leilao.propoe(lance_joao)

        quantidade_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_lances_recebido)

    # se o últime usuário for o usuário atual, não deve pertmitir propor um lance
    def test_nao_deve_permitir_propor_um_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_amanda_500 = Lance(self.amanda, 500)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_amanda)
            self.leilao.propoe(lance_amanda_500)
