numeros = [1, 2, 3, 4, 5]
soma = 0

# Primeina maneira
for numero in numeros:
    soma += numero

# Segunda maneira
sum(numeros)

print(f'A soma dos números {numeros} é: {soma}')