num = int(input('Digite um número inteiro: '))
divisores = 0

# Verificando se o número é primo
if num < 2:
    print('Não é um número primo')
else:
    for i in range(1, num+1):
        if num % i == 0:
            divisores += 1

    if divisores == 2:
        print('O número é primo')
    else:
        print('o número não é primo')