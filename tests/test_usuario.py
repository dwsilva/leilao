from leilao.leilao_project.dominio import Usuario, Leilao


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance():
    david = Usuario("David", 1000)

    leilao = Leilao("Desktop")

    david.propoe_lance(leilao, 500)

    assert david.carteira == 500


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira():
    david = Usuario("David", 1000)

    leilao = Leilao("Desktop")

    david.propoe_lance(leilao, 100)

    assert david.carteira == 900


def test_deve_permitir_lance_quando_o_valor_eh_igual_ao_valor_da_carteira():
    david = Usuario("David", 1000)

    leilao = Leilao("Desktop")

    david.propoe_lance(leilao, 1000)

    assert david.carteira == 0


def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira():
    david = Usuario("David", 1000)

    leilao = Leilao("Desktop")

    david.propoe_lance(leilao, 1001)

    assert david.carteira == 1000