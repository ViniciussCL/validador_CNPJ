import funcao_cnpj

cnpj_original = input('Insira seu CPF: ')


if funcao_cnpj.validador(cnpj_original):
    print(f'{cnpj_original} é válido')
else:
    print(f'{cnpj_original} é inválido')
