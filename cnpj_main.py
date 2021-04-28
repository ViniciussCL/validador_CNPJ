import funcao_cnpj

cnpj_original = input('Insira seu CPF: ')


if funcao_cnpj.validador(cnpj_original):
    print(f'O CNPJ:{cnpj_original} inserido é válido')
else:
    print(f'O CNPJ:{cnpj_original} inserido é inválido')
