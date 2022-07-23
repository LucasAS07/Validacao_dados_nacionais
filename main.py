#from cpf_cnpj import Documento
import re
from telefones import TelefonesBr
from datas_br import DataBr
from datetime import datetime


#cadastro = DataBr()
# print(cadastro)

hoje = DataBr()
print(hoje.tempo_cadastro())


"""def validacao_docs(numero_documento):
    doc = numero_documento
    doc = Documento.cria_docuemnto(doc)
    return print(doc)"""
