url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao +1:]

# busca o valor de um parâmetro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca) + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_parametro)

if indice_e_comercial == -1:
    parametro_origem = url_parametros[indice_parametro:]
else:
    parametro_origem = url_parametros[indice_parametro:indice_e_comercial]

print(parametro_origem)


