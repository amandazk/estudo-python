url = "https://bytebank.com/cambio?moedaOrigem=real"

indice_interrogacao = url.find('?')

url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao +1:]

print(url_base)
print(url_parametros)
