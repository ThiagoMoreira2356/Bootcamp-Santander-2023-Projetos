ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# todo: Ordenar os ativos em ordem alfabética.


#Função para organizar os ativos em ordem alfabética
def organiza_ativos():
    ativos_organizados = sorted(ativos)

    #For para percorrer cada ativo na lista e exibir em linhas separadas
    for ativo in ativos_organizados:
        print(ativo)



# todo: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
organiza_ativos()