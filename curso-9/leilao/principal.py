from dominio import Usuario, Lance, Leilao

amanda = Usuario("Amanda")
joao = Usuario("Joao")

lance_amanda = Lance(amanda, 200)
lance_joao = Lance(joao, 75)

leilao = Leilao("Computador")

leilao.lances.append(lance_amanda)
leilao.lances.append(lance_joao)

for lance in leilao.lances:
    print("O usuário {} deu um lance de {} reais".format(lance.usuario.nome, lance.valor))