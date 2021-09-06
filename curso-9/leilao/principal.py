from dominio import Usuario, Lance, Leilao, Avaliador

amanda = Usuario("Amanda")
joao = Usuario("Joao")

lance_amanda = Lance(amanda, 200)
lance_joao = Lance(joao, 75)

leilao = Leilao("Computador")

leilao.lances.append(lance_joao)
leilao.lances.append(lance_amanda)

for lance in leilao.lances:
    print("O usuário {} deu um lance de {} reais".format(lance.usuario.nome, lance.valor))

avaliador = Avaliador()
avaliador.avalia(leilao)
print("O menor lance foi de {} reais e o maior lance foi de {} reais"
      .format(avaliador.menor_lance, avaliador.maior_lance))
