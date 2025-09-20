# Função para calcular o desconto
def calcular_desconto(valor):
    VALOR_MINIMO_DESCONTO = 100
    desconto = valor * 0.1 # 10% de desconto
    valor_final = valor - desconto

    if valor >= VALOR_MINIMO_DESCONTO:
        return f'Você ganhou um desconto de 10%, pague: {valor_final}'
    else:
        return f'Você não ganhou nenhum desconto, pague: {valor}'


# Entrada de dados
valor_compra = float(input('Digite o valor da sua compra: '))

# Exibindo
print(calcular_desconto(valor_compra))