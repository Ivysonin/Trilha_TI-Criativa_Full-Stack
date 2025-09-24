IDADE_MINIMA = 18

# Entrada de dados
idade = int(input('Digite sua idade: '))

# Usando operação ternária
print('Você é maior de idade' if idade >= IDADE_MINIMA else 'Você é menor de idade')