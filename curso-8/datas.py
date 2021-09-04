import requests
from acesso_cep import BuscaEndereco

cep = 45055405
objeto_cep = BuscaEndereco(cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)

a = objeto_cep.acessa_via_cep()
print(a)