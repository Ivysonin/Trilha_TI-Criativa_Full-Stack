import time

print('') # Organização

print('=== PLANEJADOR DE VIAGEM ECONÔMICA ===')
orcamento_total = float(input('Digite o valor total disponível para a viagem (R$): '))
cidade = input('Digite a cidade de origem: ').capitalize()

print('') # Organização

print('Opções de destinos disponíveis:')
print('1 - Tamandaré')
print('2 - São José')
print('3 - Porto de Galinhas')
escolha_destino = input('Escolha o destino (1-3): ')

print('') # Organização

destinos = {
    '1': 'Tamandaré',
    '2': 'São José',
    '3': 'Porto de Galinhas'
}

sugestoes = {
    'Tamandaré': ['Praia dos Carneiros', 'Igreja de São Pedro', 'Reserva Biológica de Saltinho'],
    'São José': ['Museu Histórico', 'Parque Central', 'Feira de Artesanato'],
    'Porto de Galinhas': ['Piscinas naturais', 'Projeto Hippocampus', 'Praia de Muro Alto']
}

if escolha_destino in destinos:
    destino_escolhido = destinos[escolha_destino]

    transporte = {
        "Moto": 100,
        "Carro": 150,
        "Ônibus": 200
    }
    hospedagem = {
        "Hotel": 50,
        "Pousada simples": 100,
        "Hotel 3 estrelas": 200
    }
    custo = []

    print(f'Opções de transporte de {cidade} para {destino_escolhido}:')
    print('1 - Moto (R$ 100)')
    print('2 - Carro (R$ 150)')
    print('3 - Ônibus (R$ 200)')
    escolha_transporte = int(input('Escolha o transporte (1-3): '))

    match escolha_transporte:
        case 1:
            transporte_escolhido = 'Moto'
        case 2:
            transporte_escolhido = 'Carro'
        case 3:
            transporte_escolhido = 'Ônibus'
        case _:
            print('=== Escolha uma das opções! ===')

    custo.append(transporte[transporte_escolhido])

    print('') # Organização

    print('Opções de hospedagem por diária:')
    print('1 - Hotel (R$ 50)')
    print('2 - Pousada simples (R$ 100)')
    print('3 - Hotel 3 estrelas (R$ 200)')
    escolha_hospedagem = int(input('Escolha a hospedagem (1-3): '))

    match escolha_hospedagem:
        case 1:
            hospedagem_escolhida = 'Hotel'
        case 2:
            hospedagem_escolhida = 'Pousada simples'
        case 3:
            hospedagem_escolhida = 'Hotel 3 estrelas'
        case _:
            print('=== Escolha uma das opções! ===')

    custo_diaria = hospedagem[hospedagem_escolhida]
    custo.append(custo_diaria)

    print('') # Organização

    print('Gerando sugestão de viagem...')
    time.sleep(2)

    print('') # Organização

    print(f'Sugestão de lugares para {destino_escolhido}:')
    for lugar in sugestoes[destino_escolhido]:
        print('-', lugar)

    print('') # Organização

    dias = int(input('Quantos dias pretende ficar? '))
    gasto_total = custo[0] + (custo_diaria * dias)

    print('')
    print('=== RESUMO DO PLANO DE VIAGEM ===')
    print(f'Origem: {cidade}')
    print(f'Destino escolhido: {destino_escolhido}')
    print(f'Orçamento disponível: R$ {orcamento_total:.2f}')
    print(f'Transporte escolhido: {transporte_escolhido}')
    print(f'Hospedagem escolhida: {hospedagem_escolhida}')
    print(f'Total de dias: {dias}')
    print(f'Gasto estimado da viagem: R$ {gasto_total:.2f}')

    if gasto_total <= orcamento_total:
        print('')
        print('Viagem dentro do orçamento!')
    else:
        print('')
        print('Atenção: o plano excede o orçamento disponível.')

else:
    print('=== ESCOLHA AS OPÇÕES APRESENTADAS ===')