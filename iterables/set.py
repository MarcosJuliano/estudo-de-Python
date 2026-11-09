# set é uma lista onde n se repetem valores, util para verificações
cpf_clientes = [
    '246.217.410-98',
    '370.919.860-75',
    '394.081.930-16',
    '394.081.930-16',
    '379.649.200-22',
    '224.905.400-25',
    '446.185.200-86',
    '599.432.790-52',
    '599.432.790-52',
    '837.801.450-90'
]

set_cpf_clientes = set(cpf_clientes)
cpf_clientes_unicos = list(set_cpf_clientes)

for cpf in cpf_clientes_unicos:
    print(cpf)

print(f"temos {len(cpf_clientes)} no total.")
print(f"temos {len(cpf_clientes_unicos)} sem se repetir os clientes.")