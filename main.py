from acesso_cep import BuscaEndereco

cep = 37925000
obj = BuscaEndereco(cep)
bairro, cidade, uf = obj.acessa_via_cep()
print(f'Bairro: {bairro}, Cidade: {cidade}, UF: {uf}')

"""def validacao_docs(numero_documento):
    doc = numero_documento
    doc = Documento.cria_docuemnto(doc)
    return print(doc)"""
