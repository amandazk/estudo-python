import re # Regular Expression

endereco = "Rua Buena Vista, número 200, Boa Vista, Joinville, SC, 23440-120"
# CEP = 5 dígitos + hífen(opcional) + 3 dígitos

padrao =  re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)