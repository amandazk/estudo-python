from cpf_cnpj import CpfCnpj

cpf = ("19993663018")
documento_um = CpfCnpj(cpf, "cpf")
print(documento_um)

cnpj = "03264059000185"
documento_dois = CpfCnpj(cnpj, "cnpj")
print(documento_dois)