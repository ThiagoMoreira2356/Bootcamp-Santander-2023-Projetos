saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())


#todo: Calcular o saldo atualizado de acordo com a descrição deste desafio.
def imprime_saldo():
    saldo_atual_atualizado = (saldo_atual + valor_deposito) - valor_retirada
    print(f'Saldo atualizado na conta: {saldo_atual_atualizado}')

#todo: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
imprime_saldo()