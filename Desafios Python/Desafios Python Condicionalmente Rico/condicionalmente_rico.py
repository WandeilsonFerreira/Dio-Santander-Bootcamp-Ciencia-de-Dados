# Entrada de dados
saldo_total = int(input('Digite seu saldo: '))
valor_saque = int(input('Digite valor do saque: '))

# TODO: Criar as condições necessárias para impressão da saída, vide tabela de exemplos.
if (valor_saque <= saldo_total):
    saldo_total -= valor_saque
    print(f'Saque realizado com sucesso. Novo saldo: {saldo_total}')
else:    
    print(f'Saldo insuficiente. Saque nao realizado!')