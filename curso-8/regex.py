import re
from TelefonesBr import TelefonesBr

# padrao_molde = "(xx)aaaa-wwww"
# padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
# texto = "eu gosto do número 1245647897 e também de 5467821234"

# resposta = re.findall(padrao, texto)
# print(resposta)

telefone = "551254437621"
telefone_objeto = TelefonesBr(telefone) 

print(telefone_objeto)