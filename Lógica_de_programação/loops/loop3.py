# PRIMEIRA FORMA(mais simples)

soma = 0

for i in range(1, 10+1):
    numero = int(input(f'Digite o {i}º número inteiro: '))

    soma += numero

print("A soma de todos os números digitados vai ser:", soma)



# SEGUNDA FORMA(mais dinamica)

repeticao = int(input("Digite quantos números você quer digitar: "))
soma = 0

for i in range(1, repeticao+1):
    numero = int(input(f'Digite o {i}º número inteiro: '))

    soma += numero

print("A soma de todos os números digitados vai ser:", soma)