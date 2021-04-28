import re

formula_regressivos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def validador(cnpj):
    cnpj = formata_cnpj(cnpj)

    try:
        if sequencia(cnpj):
            return False
    except:
        return False

    try:
        novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)
        novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)
    except Exception as e:
        return False

    if novo_cnpj == cnpj:
        return True
    else:
        return False


def calcula_digito(cnpj, digito):
    if digito == 1:
        regressivos = formula_regressivos[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = formula_regressivos
        novo_cnpj = cnpj
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'


def sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


def formata_cnpj(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)
