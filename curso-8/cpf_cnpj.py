from validate_docbr import CPF, CNPJ
import validate_docbr

class CpfCnpj:
   
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if tipo_documento == "cpf":
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF Inválido")
        elif tipo_documento == "cnpj":
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ Inválido")
        else:
            raise ValueError("Tipo de documento inválido")

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.formata_cpf()
        elif self.tipo_documento == "cnpj":
            return self.formata_cnpj()
        else:
            raise ValueError("Tipo de documento inválido")

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de dígitos inválida")

    def formata_cpf(self):
       mascara = CPF()
       return mascara.mask(self.cpf)

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj) 
        else:
            raise ValueError("Quantidade de dígitos inválida")

    def formata_cnpj(self):
       mascara = CNPJ()
       return mascara.mask(self.cnpj)