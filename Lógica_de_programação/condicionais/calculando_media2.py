nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'O aluno foi aprovado com média {media}')
else:
    print(f'O aluno foi reprovado com média {media}')