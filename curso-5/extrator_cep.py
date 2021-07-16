import re # Regular Expression

endereco = "Rua Buena Vista, número 200, Boa Vista, Joinville, SC, 23440-120"
# CEP = 5 dígitos + hífen(opcional) + 3 dígitos

padrao =  re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)