ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input('Informe o numero de ativos: '))

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input('Informe o ativo: ')
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort()
print(ativos)

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.

for ativo in range(len(ativos)):
    print(f'{ativos[ativo]}')