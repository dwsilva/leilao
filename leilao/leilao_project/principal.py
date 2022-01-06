from dominio import Usuario, Lance, Leilao, Avaliador

pessoa1 = Usuario("David")
pessoa2 = Usuario("William")

lance_david = Lance(pessoa1, 500)
lance_william = Lance(pessoa2, 400)

leilao = Leilao("Notebook")

leilao.lances.append(lance_david)
leilao.lances.append(lance_william)

for lance in leilao.lances:
    print(f"O usuario {lance.usuario.nome} deu um lance de {lance.valor}")

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f"O menor lance foi de {avaliador.menor_lance}.\nO maior lance foi de {avaliador.maior_lance}.")