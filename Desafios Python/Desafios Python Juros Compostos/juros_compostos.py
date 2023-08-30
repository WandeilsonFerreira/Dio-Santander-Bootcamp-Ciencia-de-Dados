valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

def calular_taxa(x,y,z):    
    return valor_inicial*(1 + taxa_juros)**periodo

#TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros. M = C(1 + i)^t

valor_final = calular_taxa(valor_inicial,taxa_juros,periodo)

print("Valor final do investimento: R$ {:.2f}".format(valor_final))


