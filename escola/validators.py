import re

def cpf_invalido(cpf): 
    return len(cpf) != 11

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    # 83 99999-9999
    return not bool(re.search(r'^\d{2}\s\d{5}-\d{4}$', celular))
#
# The code above is a validator that checks if the CPF, name, and cell phone number are valid.  