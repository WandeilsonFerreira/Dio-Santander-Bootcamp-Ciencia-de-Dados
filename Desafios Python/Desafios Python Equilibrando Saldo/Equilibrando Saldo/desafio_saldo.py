saldo_atual = float(input('Informe o saldo atual do funcionário: '))
valor_deposito = float(input('Informe o valor de depósito: '))
valor_retirada = float(input('Informe o valor do saque: '))

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_atual += valor_deposito
saldo_atual -= valor_retirada

#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print(f'Saldo atualizado na conta: {saldo_atual:.1f} ')