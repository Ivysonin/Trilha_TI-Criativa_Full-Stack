# Entrada de dados
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

# Calculando
media = (num1 + num2 + num3) / 3
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

# Exibindo
print(f'Média: {round(media, 2)}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')