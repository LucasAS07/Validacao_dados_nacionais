#from cpf_cnpj import Documento
import re
from telefones import TelefonesBr

tel = '553798026179'
telefone_objeto = TelefonesBr(tel)
print(telefone_objeto)

"""def validacao_docs(numero_documento):
    doc = numero_documento
    doc = Documento.cria_docuemnto(doc)
    return print(doc)"""
