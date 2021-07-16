import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.limpa_url(url)
        self.valida_url()

    def limpa_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?(bytebank.com)(.br)?(/cambio)')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao +1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca) 
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_parametro)

        if indice_e_comercial == -1:
           valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

    def converte(self):
        cotacao_dolar = 5.50
        origem = self.get_valor_parametro("moedaOrigem")
        destino = self.get_valor_parametro("moedaDestino")
        quantidade = float(self.get_valor_parametro("quantidade"))

        if origem == "dolar" and destino == "real":
            valor_conversao = quantidade * cotacao_dolar
            return valor_conversao

        elif origem == "real" and destino == "dolar":
            valor_conversao =  quantidade / cotacao_dolar
            return valor_conversao

url = 'https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100'
extrator = ExtratorURL(url)
valor_quantidade = extrator.get_valor_parametro("moedaOrigem")
print(extrator)
print(valor_quantidade)
print("O tamanho da URL é:", len(extrator))

extrator_2 = ExtratorURL(url)
print(extrator_2 == extrator)
# imprimir o endereço de memória
print(id(extrator))
print(id(extrator_2))

# Desafio
valor_convertido = extrator.converte()
print("O valor convertido é : {:.2f}".format(valor_convertido))
