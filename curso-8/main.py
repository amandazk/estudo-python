from cpf_cnpj import Documento

cpf = ("19993663018")
documento_um = Documento.cria_documento(cpf)
print(documento_um)

cnpj = "03264059000185"
documento_dois = Documento.cria_documento(cnpj)
print(documento_dois)