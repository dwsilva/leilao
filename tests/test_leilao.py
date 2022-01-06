from unittest import TestCase

from leilao.excecoes import LanceInvalido
from leilao.leilao_project.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_david)
            self.leilao.propoe(self.lance_william)



    def test_deve_retornar_o_maior_e_o_menor_valor_quando_leilao_possuir_tres_lances_(self):
        with self.assertRaises(LanceInvalido):
            pessoa3 = Usuario("David William", 500)
            lance_david_william = Lance(pessoa3, 400)

            self.leilao.propoe(self.lance_william)
            self.leilao.propoe(self.lance_david)
            self.leilao.propoe(lance_david_william)


    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_possua_lances(self):
        self.leilao.propoe(self.lance_david)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        with self.assertRaises(LanceInvalido):
            pessoa4 = Usuario("Nova Pessoa", 500)
            lance_nova_pessoa = Lance(pessoa4, 350)

            self.leilao.propoe(self.lance_david)
            self.leilao.propoe(lance_nova_pessoa)

            quantidade_de_lances_recebido = len(self.leilao.lances)

            self.assertEqual(2, quantidade_de_lances_recebido)


    def test_nao_deve_permitir_propor_lance_caso_usuario_seja_o_mesmo(self):
        lance_david_novo = Lance(self.pessoa1, 390)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_david)
            self.leilao.propoe(lance_david_novo)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_david)
            self.leilao.propoe(self.lance_william)

    def setUp(self):
        self.pessoa1 = Usuario("David", 500)
        self.pessoa2 = Usuario("William", 500)

        self.lance_david = Lance(self.pessoa1, 500)
        self.lance_william = Lance(self.pessoa2, 400)

        self.leilao = Leilao("Notebook")

