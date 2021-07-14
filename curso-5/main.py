url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

indice_interrogacao = url.find('?')
url_parametros = url[indice_interrogacao +1:]

parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca) + len(parametro_busca) + 1
parametro_origem = url_parametros[indice_parametro:]
print(parametro_origem)


