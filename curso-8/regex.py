import re

padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "amanda opa, tudo bem? amanda@gmail.com.br  opa, beleza?"
resposta = re.search(padrao, texto)
print(resposta.group())